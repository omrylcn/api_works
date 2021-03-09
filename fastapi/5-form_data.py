from fastapi import FastAPI,Form
import uvicorn

app=FastAPI()


@app.post("/login/")
def login(*, username: str = Form(...), password: int = Form(...)):
    
    new_password=100+password
    return {"username": username,"new_pasword":new_password}


if __name__=="__main__":
    uvicorn.run(app ,port=5000)