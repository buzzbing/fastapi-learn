# To send data, you should use one of: POST (the more common), PUT, DELETE or PATCH.
# Sending a body with a GET request has an undefined behavior in the specifications, 
# nevertheless, it is supported by FastAPI, only for very complex/extreme use cases.

from fastapi import FastAPI,APIRouter
from pydantic import BaseModel

app = FastAPI()
router = APIRouter()

class Item(BaseModel):
    name: str
    description: str | None = None #Use None to make it just optional.
    price: float
    tax: float | None = None
@app.get('/')
async def main():
    return {"message":"hello"}

@app.post('/items')
async def create_item(item:Item):
    return item