from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

@app.get('/')
def index():
    return {"Hello": "world1"}

@app.post("/items/")
async def create_item(item: Item):
    return item


