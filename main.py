from typing import Optional
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from numpy import block
import pandas as pd
import sys 
from typing import Union


import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="./server/static"), name="static")

templates = Jinja2Templates(directory="./server/templates")


@app.get("/", response_class=HTMLResponse)
async def dash(request: Request):

    context = {"request": request, "data":'helloword'}
    return templates.TemplateResponse("main.html",context)

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
    for i in buoy_id:
        data_total[int(i)] =  alldata_height[buoy_template[int(i)]][start_index:end_index].to_list()
        
        

    
    # context = {"request": request,"buoy_id":buoy_id, "data_period":data_period, "data_height":data_height, "data_direction":data_direction}
    # jsonable_encoder(data)
    # context = {"request": request, "data":data}
    res = jsonable_encoder({"data":data_total})

    return JSONResponse(content=res)
    # return  templates.TemplateResponse("chart.html", context)



if __name__ == "__main__":
    uvicorn.run(app, host ="0.0.0.0", port = 8002 ) 
