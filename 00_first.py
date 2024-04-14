from fastapi import FastAPI

app = FastAPI()

# # get data from path and return  '/'
@app.get('/')
async def root():
    return{'message':'hello'}

#  run on terminal $ uvicorn 00_first:app --reload
