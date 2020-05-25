from fastapi import FastAPI
import uvicorn

app=FastAPI()


@app.get("/")
def run_item():
    return {"deneme":"merhana"}

if __name__=="__main__":
    uvicorn.run(app,port=8000)