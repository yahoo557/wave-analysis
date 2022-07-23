# 뷰티풀수프와 셀레늄을 활용하여 권한 없는 '공공데이터 API' 기능 구현하기.
# 속도와 트래픽에서 차이가 있을수 있지만, 30분 단위로 최신화 할수 있는
# 방법이 이것 뿐인듯 ㅠㅠ

from matplotlib.font_manager import json_dump
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pymongo import MongoClient
from datetime import datetime
import json
########################################
#  울릉도, 동해, 동해78, 울진, 울산, 포항 의   #
#  해양부이로 부터 얻은 최대,유의,평균 파고와    #
#  파주기, 파향을 30분 마다 DB에 저장한다      #
########################################


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument("disable-gpu")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def get_half_time():
    time_now = datetime.now().timestamp()
    halftime= time_now - time_now%1800
    return halftime

# # 1) DB의 가장 최근 date와 현재 시간보다 30분이 지났는지 비교한다.

db_client = MongoClient("mongodb://localhost:27017/")
db = db_client['buoy']['daily']
date_now = datetime.now().timestamp()

index = {'울릉도':1, "동해":6, "포항":7, "울산": 16, "울진":17, "동해78":26}
if str(db.find_one({"date":get_half_time()})) == 'None':
#울릉도, 동해, 동해78, 울진, 울산, 포항 해양 기상 부이 30분 마다 스크래핑
    driver = set_chrome_driver()
    url = 'https://www.weather.go.kr/w/obs-climate/sea/buoy.do'
    driver.get(url) 

    date = driver.find_element("xpath",'//*[@id="sea-buoy-data-holder"]/p').get_attribute("innerHTML")
    date_format = "%Y년 %m월 %d일 %H시 %M분"
    datetime_timestamp = datetime.strptime(date[14:], date_format).timestamp()

    # 2) date가 서로 다르다면 data가 갱신된것으로 간주, 스크래핑을 한다.
    # 참고 : 각기상부이 데이터별 xpath <tr>태그 인덱스 : 울릉도, 동해, 포항, 울산, 울진, 동해78 순으로 : 1, 6, 7, 17, 26 
    if(get_half_time()==datetime_timestamp):
        db_format = {"date" : datetime_timestamp}
        for i in index:
            element_dict = {}
            element_key = ["maximum", "significant", "mean", "period", "direction"]
            k = index.get(i)
            if k == 1 :
                for j in range (5):
                    element_dict[element_key[j]] = driver.find_element("xpath",'//*[@id="sea-buoy-data-holder"]/table/tbody/tr[%d]/td[%d]'% (k, j+10)).get_attribute("innerHTML")
            else:
                for j in range (5):
                    element_dict[element_key[j]] = driver.find_element("xpath",'//*[@id="sea-buoy-data-holder"]/table/tbody/tr[%d]/td[%d]'% (k, j+9)).get_attribute("innerHTML")
            db_format[i] = element_dict
            
        # 3) 스크래핑 해온 데이터를 DB에 저장.
        db.insert_one(db_format)
        print(get_half_time(),": 최신화를 완료했습니다.")    
        driver.quit()
    else:
        print(get_half_time(),": 웹에 데이터가 갱신되지 않았습니다.")
else:
    print(get_half_time(),": 최신상태입니다.")    











