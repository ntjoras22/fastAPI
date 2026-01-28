from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hi, FastAPI is working!"}


@app.get("/hello")
def read_hello():
    return {"message": "Hello, FastAPI is working!"}    


@app.get("/items/{item_id}")
def read_item(item_id: int, q: int):
    return {"item_id": item_id, "q": q}
