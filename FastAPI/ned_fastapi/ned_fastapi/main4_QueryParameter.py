from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get('/')
def index():
    return {"Hello": "world1"}


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]