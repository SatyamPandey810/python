from fastapi import FastAPI,Query,HTTPException
from fastapi.responses import JSONResponse
import json
app=FastAPI()
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal

class Patient(BaseModel):
    id:Annotated[str, Field(...,description='Id of the patients',examples=['1'])]
    name:Annotated[str,Field(...,description='name of the patients')]
    city:Annotated[str,Field(...,description="City is")]
    age:Annotated[int,Field(...,gt=0,lt=120,description="age is")]
    gender:Annotated[Literal['male','female','other'],Field(...,description="Gender of the patients")]
    height:Annotated [float,Field(...,gt=0,description="Height of the patients")]
    weight:Annotated[float,Field(...,description="Weight of the patients in KG")]
    
    @computed_field
    @property
    def bmi(self)->float:
          bmi =round(self.weight/(self.height**2),2)
          return bmi
      
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<18.5:
            return "under weight"
        elif self.bmi <25:
            return "Normal"    

        elif self.bmi<30:
            return "Normal"    
        else:
            return "Obese"
      


# @app.get("/")
# def hello():
#     return {"message":"hello world"}
    
# @app.get("/about")
# def about():
#     return {"message":"this is about page"}

# -------------------------

def load_data():
    try:
        with open("patients.json") as f:
          return json.load(f)
    except FileNotFoundError:
        return {}
      
    return data    

# @app.get("/")
# def view(): 
#     data=load_data()
#     return data


# # # Path parameter
# @app.get("/patient/{patient_id}")
# def view_patient(patient_id:str):
#   data=load_data()    
#   if patient_id in data:
#       return data[patient_id]
# raise HTTPException(status_code=404,detail="Not Found is")   

#Query parameter
# @app.get('/sort')
# def sort_patients(sort_by:str=Query(...,description='sort on the basic'),order:str=Query('asc',description='short on assending and desc order')):
#     valid_fields=['height','age  ','bmi']
#     if sort_by not in valid_fields: 
#        raise HTTPException(status_code=400,detail=f'Invalid fields select from {valid_fields}')
#     if order not in ['asc','desc']:
#         raise HTTPException(status_code=400,detail='Inalid order select between asc and dsc')
    
# data=load_data()
# sort_order =True if order=='desc' else False
# shorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
# return shorted_data


def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)

      
@app.post("/create")
def create_patients(patients:Patient):
    # Load existing data
    data=load_data()
    
    # check if the patients alerady exists
    if patients.id in data:
        raise HTTPException(status_code=400,detail="Patienst already exists")
    
    # new patients add to the database
    data[patients.id] = patients.model_dump(exclude=['id'])
    save_data(data)
    return JSONResponse(status_code=201,content={'message':"patients created successfully"})

    
    
    