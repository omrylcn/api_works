from fastapi import FastAPI,Form
import uvicorn

app=FastAPI()


@app.post("/login/")
def login(*, username: str = Form(...), password: str = Form(...)):
    return {"username": username}


if __name__=="__main__":
    uvicorn.run(app ,port=5000)