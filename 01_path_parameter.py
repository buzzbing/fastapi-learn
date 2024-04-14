from fastapi import FastAPI

app = FastAPI()

# This function demonstrates the passing of parameter
# Here, through path as {item_id} which is returned by the read_item function
# datatype of path parameter can also be defined in the read_item function

# the path having constant or fixed parameters must be declared before variable parameter
# this avoids overriding of parameters

@app.get('/')
async def root():
    return {"message":"This is root."}

@app.get("/items/home")
async def read_item():
    return {"message": "This is home."}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# If you have a path operation that receives a path parameter,
# but you want the possible valid path parameter values to be predefined, you can use a standard Python Enum.

from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "This is from path alexnet"}
    if model_name.value == 'lenet':
        return {"model_name":model_name, "message": "this is from path lenet"}
    
    return {"model_name":model_name,"message": "This is from default path"}
