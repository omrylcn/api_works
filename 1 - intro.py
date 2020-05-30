from fastapi import FastAPI
import uvicorn

app=FastAPI()


@app.get("/")
def run_item():
    return {"test":"merhaba"}

if __name__=="__main__":
    uvicorn.run(app,port=5000)

# go  http://127.0.0.1:5000/docs
# alternative http://127.0.0.1:5000/redoc

# 
"""
RECAP 

Import FastAPI.
Create an app instance.
Write a path operation decorator (like @app.get("/")).
Write a path operation function (like def root(): ... above).
"""