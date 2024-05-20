from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get('/')
def index():
    return {"Hello": "world1"}


@app.post("/items/{name}")
def fn_items(name):
    return {"purchase item":name}