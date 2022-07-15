from typing import Optional
from fastapi import FastAPI

import uvicorn



app = FastAPI()

@app.get("/items/{item_id}")



def read_item(home_id:int, away:id ,q:Optional[str]= None):
    return {"item_id":home_id,  "q":q}

if __name__ == "__main__":
    uvicorn.run(app, host ="0.0.0.0", port = 8001 ) 

