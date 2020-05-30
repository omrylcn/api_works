"""
When you declare other function parameters that are not part of the path parameters,
they are automatically interpreted as "query" parameters.

"""

import uvicorn
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"},
 {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
def read_item(skip:int=20):
    return skip

if __name__ =="__main__":
    uvicorn.run(app,port=5000)