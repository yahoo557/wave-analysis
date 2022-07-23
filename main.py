from typing import Optional
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

import uvicorn



app = FastAPI()

@app.get("/items/{item_id}")



def read_item():
    return {}

if __name__ == "__main__":
    uvicorn.run(app, host ="0.0.0.0", port = 8001 ) 

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

# 30분마다 1분간격으로 데이터가 추가될동안 스크래핑 컨트롤러 호출
#   while server.on and :
#