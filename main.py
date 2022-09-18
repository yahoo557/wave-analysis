from typing import Optional
from urllib import request
from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_utils.tasks import repeat_every
import matplotlib.pyplot as plt
from numpy import block
import numpy as np
import pandas as pd
import sys 
from typing import Union
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pymongo import MongoClient
from datetime import datetime

import json
import time
import uvicorn



app = FastAPI()

app.mount("/static", StaticFiles(directory="./server/static"), name="static")

templates = Jinja2Templates(directory="./server/templates")


@app.get("/", response_class=HTMLResponse)
async def dash(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("main.html",context)


# 그래프 출력에 필요한 데이터를 슬라이싱해서 main.html에 전달함
@app.get("/buoy/")
async def read_item(request: Request, buoy_id: str, start:str, end:str,  q: Union[str, None] = None):
    data_total = {}
    buoy_template = {1:"울릉도", 2:"동해", 3:"포항", 4:"울산", 5:"울진", 6:"동해78"}
    alldata_period = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_파주기_통합본.csv",encoding='cp949')
    alldata_period = alldata_period.fillna(0)
    alldata_height = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_유의파고_통합본.csv" ,encoding='cp949')
    alldata_height = alldata_height.fillna(0)
    alldata_direction = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_파향_통합본.csv" ,encoding='cp949')
    alldata_direction = alldata_direction.fillna(0)
    start_index = alldata_height.loc[alldata_height["일시"]=="%s 00:00" %start].index.values[0]
    end_index = alldata_height.loc[alldata_height["일시"]=="%s 00:00" %end].index.values[0]
    if(end):
        data_total['date'] = alldata_period['일시'][start_index:end_index].to_list()
        for i in buoy_id:
            data_total[int(i)] =  alldata_height[buoy_template[int(i)]][start_index:end_index].to_list()
            
    else :
        data_total['date'] = alldata_period['일시'][start_index:].to_list()
        for i in buoy_id:
            data_total[int(i)] =  alldata_height[buoy_template[int(i)]][start_index:].to_list()

    
    # context = {"request": request,"buoy_id":buoy_id, "data_period":data_period, "data_height":data_height, "data_direction":data_direction}
    # jsonable_encoder(data)
    # context = {"request": request, "data":data}
    res = jsonable_encoder({"data":data_total})

    return JSONResponse(content=res)
    # return  templates.TemplateResponse("chart.html", context)

def set_chrome_driver():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        chrome_options.add_argument("disable-gpu")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        return driver

def get_half_time():
    time_now = datetime.now().timestamp()
    halftime_timestamp= time_now - time_now%1800
    halftime = datetime.fromtimestamp(halftime_timestamp)
    return halftime
url = 'https://www.weather.go.kr/w/obs-climate/sea/buoy.do'

@app.get("/live/")
async def read_item(request: Request, buoy_id: str, q: Union[str, None] = None):
    
    # {"울릉도":1, "동해":6, "포항":7, "울산": 16, "울진":17, "동해78":26}
    # url 파라미터로 전달 받은 부이들의 인덱스만 index[] 변수에 저장한다.
    index_template = [1, 6, 7, 16, 17, 26]
    index = []
    for i in range(len(buoy_id)) :
        index.append(index_template[int(buoy_id[i])-1])
    
    #울릉도, 동해, 동해78, 울진, 울산, 포항 해양 기상 부이 30분 마다 스크래핑
    driver = set_chrome_driver()
    
    driver.get(url) 
    date = driver.find_element("xpath",'//*[@id="sea-buoy-data-holder"]/p').get_attribute("innerHTML")
    date_format = "%Y년 %m월 %d일 %H시 %M분"
    # datetime_timestamp = datetime.strptime(date[14:], date_format).timestamp()

    # 스크래핑 
    # if(get_half_time()==datetime_timestamp):
    
    scraped_data = {}
    element_key = ["significant", "period", "direction"]
    for i in index:
        element_dict = {}
        if i == 1:
            element_dict[element_key[0]] = driver.find_element("xpath",'//*[@id="sea-buoy-data-holder"]/table/tbody/tr[%d]/td[%d]'% (i, 11)).get_attribute("innerHTML")    
            element_dict[element_key[1]] = driver.find_element("xpath",'//*[@id="sea-buoy-data-holder"]/table/tbody/tr[%d]/td[%d]'% (i, 13)).get_attribute("innerHTML")    
            element_dict[element_key[2]] = driver.find_element("xpath",'//*[@id="sea-buoy-data-holder"]/table/tbody/tr[%d]/td[%d]'% (i, 14)).get_attribute("innerHTML")    
        else :
            element_dict[element_key[0]] = driver.find_element("xpath",'//*[@id="sea-buoy-data-holder"]/table/tbody/tr[%d]/td[%d]'% (i, 10)).get_attribute("innerHTML")
            element_dict[element_key[1]] = driver.find_element("xpath",'//*[@id="sea-buoy-data-holder"]/table/tbody/tr[%d]/td[%d]'% (i, 12)).get_attribute("innerHTML")
            element_dict[element_key[2]] = driver.find_element("xpath",'//*[@id="sea-buoy-data-holder"]/table/tbody/tr[%d]/td[%d]'% (i, 13)).get_attribute("innerHTML")
        scraped_data[i] = element_dict     
    scraped_data['date'] = get_half_time()
    
    data_total = scraped_data
    
    res = jsonable_encoder({"data":data_total})
    return JSONResponse(content=res)




# csv파일에 최신 데이터 update하는 background task
@app.on_event("startup")
@repeat_every(seconds = 10)
def scheduled_task() -> None:
    time_now = datetime.now()
    alldata_height = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_유의파고_통합본.csv" ,encoding='cp949')
    csv_last_date = alldata_height.tail(1)['일시'].values[0]
    date_format = "%Y.%m.%d %H:%M"
    csv_list_date_timestamp = datetime.strptime(csv_last_date, date_format).timestamp()

# 매시 30분, 정각 마다 스케쥴링
    if (time_now.minute == 30 or time_now.minute == 00):
        while True :
            driver = set_chrome_driver()
            driver.get(url) 
            scrapping_raw_date = driver.find_element("xpath",'//*[@id="sea-buoy-data-holder"]/p').get_attribute("innerHTML")
            
            date_format = "%Y년 %m월 %d일 %H시 %M분"
            scrapping_date = datetime.strptime(scrapping_raw_date[14:], date_format).timestamp()

            #csv의 최신데이터와 방금 막 기상청에서 받아온 데이터와의 시간이 일치하지 않는다면 csv가 업데이트 되어야 한다는것으로 간주
            if(csv_list_date_timestamp != scrapping_date):
                scraped_data = {}
                element_key = ["significant", "period", "direction"]
                element_dict = {}
                element_dict[element_key[0]] = driver.find_element("xpath",'//*[@id="sea-buoy-data-holder"]/table/tbody/tr[%d]/td[%d]'% (1, 11)).get_attribute("innerHTML")    
                element_dict[element_key[1]] = driver.find_element("xpath",'//*[@id="sea-buoy-data-holder"]/table/tbody/tr[%d]/td[%d]'% (1, 13)).get_attribute("innerHTML")    
                element_dict[element_key[2]] = driver.find_element("xpath",'//*[@id="sea-buoy-data-holder"]/table/tbody/tr[%d]/td[%d]'% (1, 14)).get_attribute("innerHTML")    
                scraped_data[1] = element_dict
                for i in range(2,5):
                    element_dict[element_key[0]] = driver.find_element("xpath",'//*[@id="sea-buoy-data-holder"]/table/tbody/tr[%d]/td[%d]'% (i, 10)).get_attribute("innerHTML")
                    element_dict[element_key[1]] = driver.find_element("xpath",'//*[@id="sea-buoy-data-holder"]/table/tbody/tr[%d]/td[%d]'% (i, 12)).get_attribute("innerHTML")
                    element_dict[element_key[2]] = driver.find_element("xpath",'//*[@id="sea-buoy-data-holder"]/table/tbody/tr[%d]/td[%d]'% (i, 13)).get_attribute("innerHTML")
                    scraped_data[i] = element_dict     
                
                print(element_dict)
                break
            else :
                print("not yet")
                time.sleep(60)    
        
@app.get('/matplot')
def mat_video():
    from numpy import block
    import os
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import time
    import mpld3
    import math
    from matplotlib import animation, font_manager, rc
    from IPython.display import HTML
    from matplotlib.animation import FuncAnimation


    alldata = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_파주기_통합본.csv",encoding='cp949')
    alldata_height = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_유의파고_통합본.csv" ,encoding='cp949')
    # 전체 데이터 중 주기의 최댓값 찾기
    themax = 0
    for i in range(2,8):
        heremax = max(alldata.iloc[:,i])
        if heremax >= themax: themax = heremax



    # 파주기, 유의파고가 있는 통합본 불러오기, fillna로 nan값 0으로
    data_perod = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_파주기_통합본.csv", encoding='cp949')
    data_perod = data_perod.fillna(0)
    data_height = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_유의파고_통합본.csv", encoding='cp949')
    data_height = data_height.fillna(0)
    data_direction = pd.read_csv("/Users/seungbaek/Desktop/호텔/파도분석/data/combineddata/동해바다_파향_통합본.csv", encoding='cp949')
    data_direction = data_direction.fillna(0)
    data_perod['일시'] = pd.to_datetime(data_perod['일시'])
    data_height['일시'] = pd.to_datetime(data_height['일시'])



    def init():
        
        plt.ylim([-9, 9])
        plt.xlim(0,700)
        return fig,

    def animate(i):
        plt.clf()    
        selcetion = ['울릉도', '동해', '동해78', '포항', '울산', '울진']
        title = ['Uleung', 'Donghae', 'Donghae78', 'Pohang', 'Ulsan', 'Uljin']
        
        for t in range(1,6):
            ax = fig.add_subplot(int('51%s'%(str(t))))
            ax.set_title(title[t-1])
            k=0
            tick_x = [50,150,250,350,450,550,650]
            if t!= 5:
                plt.xticks(visible=False)
                plt.ylim([-10, 10])
            else :
                
                plt.ylim([-10, 10])
                plt.xlim([0,700])
                
                
            date = []    
            for j in range(i+100000, i+100007):
                percentage = data_perod[selcetion[t]][j]/themax
                date.append(data_perod['일시'][j])
                x0 = int(100*(1-percentage)/2)+k*100
                x1 = int((100*percentage)/3+x0)
                x2 = int((100*percentage)*2/3+x0)
                x3 = int((100*percentage)+x0)
                plt.plot([x0,x1],[0,data_height[selcetion[t]][j]], color='green')
                plt.plot([x1,x2],[data_height[selcetion[t]][j],-data_height[selcetion[t]][j]], color='green')
                plt.plot([x2,x3],[-data_height[selcetion[t]][j],0], color ='green')
                plt.quiver(tick_x[k],5, data_direction[selcetion[t]][j]  ,data_perod[selcetion[t]][j])
                k+=1
            if t == 5:
                ax.set_xticks(tick_x, date, fontsize = 4)
                


            

    fig = plt.gcf()

    # fig, axes = plt.subplots(nrows=5, ncols=1)

    anim = FuncAnimation(fig=fig, func=animate, init_func=init, interval=1000)

    # plt.show()
    if os.path.isfile('/Users/seungbaek/Desktop/호텔/파도분석/server/templates/chart.html'):
        os.remove('/Users/seungbaek/Desktop/호텔/파도분석/server/templates/chart.html', )

    # rc('animation', html='jshtml')
    # rc
    f = open('/Users/seungbaek/Desktop/호텔/파도분석/server/templates/chart.html', 'w')
    f.write('''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">    
        <title>chart</title>
    </head>
    '''
    )
    f.write(HTML(anim.to_jshtml()).data)
    f.write('''
    <body>
        
    </body>

    </html>'''
    )
    f.close
    # context = {"request": '200'}
    return True




@app.get("/matplot_video", response_class=HTMLResponse)
def mat_video(request: Request):
    
    return templates.TemplateResponse("chart.html",{"request":request})


if __name__ == "__main__":
    uvicorn.run(app, host ="0.0.0.0", port = 8002 ) 
