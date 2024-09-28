from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/api/')
def read_root():
    return {"Hello World": "Beautiful"}

@app.get('/items/{item_id}')
def read_item(item_id: int):
    return {"item_id": item_id}