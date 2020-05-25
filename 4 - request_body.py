from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class Item(BaseModel):
    name:str
    description:str = None
    price : float
    tax: float = None

app=FastAPI()

i = None

@app.post("/post_items/")
def create_item(item:dict):
    global i
    i=item
    print("deneme") 
    return item

@app.get("/get_items/")
def get_item():
    print(i)
    return i


if __name__ =="__main__":
    uvicorn.run(app,port=5000)

