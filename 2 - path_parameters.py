# You can declare path "parameters" or "variables" with the same syntax used by Python format strings

from fastapi import FastAPI
import  uvicorn

app=FastAPI()

@app.get("/items/{arg_id}")
def read_item(arg_id:int):
    
    try:
        assert type(arg_id)==int ,"unvalid arg type"

        return {"item_id":arg_id}
    
    except Exception as e:
       
        return "Error : {}".format(e)
if __name__ =="__main__":
    uvicorn.run(app,port=5000)


# The value of the path parameter arg_id will be passed to your function as the argument item_id.
# go to  http://127.0.0.1:5000/items/foo