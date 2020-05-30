# https://stackoverflow.com/questions/60783222/how-to-test-a-fastapi-api-endpoint-that-consumes-images
#https://stackoverflow.com/questions/24033960/saving-image-in-a-temporary-file-in-django
#https://stackoverflow.com/questions/55873174/how-do-i-return-an-image-in-fastapi

from fastapi import FastAPI, File, UploadFile
import uvicorn 
from PIL import Image


a=None
app = FastAPI(reload=True,debug=True)


@app.post("/files/")
def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
def create_upload_file(file: UploadFile = File(...)):
    a=file.file
    #print(a.read())
    i=Image.open(a)
    
    i.show()
    print(type(i))
    return file.filename#{"filename": file.filename}


if __name__ =="__main__":
    uvicorn.run(app,port=5000)#£,reload=True)