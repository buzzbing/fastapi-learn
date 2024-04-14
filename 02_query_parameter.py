# When you declare other function parameters that are not part of the path parameters,
#  they are automatically interpreted as "query" parameters.

from fastapi import FastAPI

app = FastAPI()

items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return items_db[skip : skip + limit]


# for example path http://127.0.0.1:8000/items/?skip=1&limit=10 will skip first item
# As query parameters are not a fixed part of a path, they can be optional and can have default values
#  here skip=0 and limit=10


# Optional parameters
# declare optional query parameters, by setting their default to None
# here q is optional
@app.get("/items/{item_id}")
async def read_item(
    item_id: str,
    q: str | None = None,
):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# Query parameter type conversion
@app.get("/items_again/{item_id}")
async def read_item(
    item_id: str,
    q: str | None = None,
    short :bool = False,
):
    item = {"item_id":item_id}
    if q: 
        item.update({"q":q})
    if short:
        item.update({"description":"query parameter conversion"})
    return item
