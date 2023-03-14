from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return {"Hello World ❤"}

#path parameters

@app.get("/items/{item_id}")
def read_item(item_id:str):
    return {"item_id": item_id}