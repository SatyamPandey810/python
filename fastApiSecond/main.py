from fastapi import FastAPI,Query,HTTPException
import json
app=FastAPI()

# @app.get("/")
# def hello():
#     return {"message":"hello world"}
    
# @app.get("/about")
# def about():
#     return {"message":"this is about page"}

# -------------------------

def load_data():
    with open("patients.json") as f:
        data=json.load(f)
        
    return data    

@app.get("/")
def view(): 
    data=load_data()
    return data


# Path parameter
@app.get("/patient/{patient_id}")
def view_patient(patient_id:str):
  data=load_data()    
  if patient_id in data:
      return data[patient_id]
# raise HTTPException(status_code=404,detail="Not Found is")   

#Query parameter
@app.get('/sort')
def sort_patients(sort_by:str=Query(...,description='sort on the basic'),order:str=Query('asc',description='short on assending and desc order')):
    valid_fields=['height','age  ','bmi']
    if sort_by not in valid_fields: 
       raise HTTPException(status_code=400,detail=f'Invalid fields select from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Inalid order select between asc and dsc')
    
    data=load_data()
    sort_order =True if order=='desc' else False
    shorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)

    return shorted_data
