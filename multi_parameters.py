from fastapi import FastAPI
import uvicorn

app=FastAPI()


@app.get("/users/{item1}/{item2}")
def run_item(item1,item2:int=20):
    return {"item_return":(item1,item2)}

if __name__=="__main__":
    uvicorn.run(app,port=8000)