from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pymongo


app=FastAPI()
app.mount('/static',StaticFiles(directory='static'),name='static')
templates=Jinja2Templates(directory='templates')

# connection mongodb
client = pymongo.MongoClient("mongodb://localhost:27017")
database=client["fastApi"]
collection=database["fast_api"]

@app.get('/{name}',response_class=HTMLResponse)
def home(request:Request,name):
    collection.insert_one({'name':name})
    return templates.TemplateResponse(
        request=request,name='index.html'
    )

@app.get('/about',response_class=HTMLResponse)
def home(request:Request):
    return templates.TemplateResponse(
        request=request,name='about.html'
    )

