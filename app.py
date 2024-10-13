from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def main():
    return {"Hello": "World!"}


@app.get("/items/{item_id}")
def items(item_id: int):
    return {"item_id": item_id}
