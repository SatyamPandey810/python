from fastapi import FastAPI,Query,HTTPException
from fastapi.responses import JSONResponse
import json
app=FastAPI()
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal,Optional

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
      
class PatientUpdate(BaseModel):
    name:Annotated[Optional[str],Field(default=None)]
    city:Annotated[Optional[str],Field(default=None)]
    age:Annotated[Optional[int],Field(default=None,gt=0)]
    gender:Annotated[Optional[Literal['male','female']],Field(default=None)]
    height:Annotated [Optional[float],Field(default=None,gt=0)]
    weight:Annotated[Optional[float],Field(default=None,gt=0)]
    

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

## for update
from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

app = FastAPI()


class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Id of the patients", examples=["1"])]
    name: Annotated[str, Field(..., description="Name of the patient")]
    city: Annotated[str, Field(..., description="City")]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age")]
    gender: Annotated[Literal["male", "female", "other"], Field(..., description="Gender")]
    height: Annotated[float, Field(..., gt=0, description="Height in meters")]
    weight: Annotated[float, Field(..., gt=0, description="Weight in KG")]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height**2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"


class PatientUpdate(BaseModel):  # FIX: Inherit from BaseModel
    name: Optional[str] = None
    city: Optional[str] = None
    age: Optional[int] = Field(default=None, gt=0, lt=120)
    gender: Optional[Literal["male", "female", "other"]] = None
    height: Optional[float] = Field(default=None, gt=0)
    weight: Optional[float] = Field(default=None, gt=0)


# ----------------- Helpers -----------------
def load_data():
    try:
        with open("patients.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)


# ----------------- Routes -----------------
# create
@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")

    data[patient.id] = patient.model_dump(exclude={"id"})
    save_data(data)

    return JSONResponse(
        status_code=201, content={"message": "Patient created successfully"}
    )

# update
@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, patient_update: PatientUpdate):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    # Get existing patient data
    existing_patient_info = data[patient_id]

    # Apply updates (only provided fields)
    updates = patient_update.model_dump(exclude_unset=True)
    for key, value in updates.items():
        existing_patient_info[key] = value

    # Validate with Patient model
    updated_patient = Patient(id=patient_id, **existing_patient_info)

    # Save updated data
    data[patient_id] = updated_patient.model_dump(exclude={"id"})
    save_data(data)

    return {"message": "Patient updated successfully", "patient": updated_patient}


# Delete 
@app.delete('/delete/{patient_id}')
def delete_patient(patient_id=str):
    data=load_data()  

    if patient_id not in data:
        raise HTTPException(status_code=404,detail='patients not found')

    del data[patient_id]
    save_data(data)

    return JSONResponse(status_code=200,content='patients deleted')
    