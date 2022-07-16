from typing import Optional
from fastapi import FastAPI

import uvicorn



app = FastAPI()

@app.get("/items/{item_id}")



def read_item(home_id:int, away:id ,q:Optional[str]= None):
    return {"item_id":home_id,  "q":q}

if __name__ == "__main__":
    uvicorn.run(app, host ="0.0.0.0", port = 8001 ) 


# 30분마다 1분간격으로 데이터가 추가될동안 크롤링 컨트롤러 호출
#   while server.on and :
#