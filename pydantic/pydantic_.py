from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

# def insert_petient_data(name,age):    
#     if type(name)==str and type(age)==int:        
#      print(name)
#      print(age)
#     else:
#         print("somthing went wrong")  

# insert_petient_data('john',"12")

# class Patients(BaseModel):
#     name:str
#     age:int 

# def insert_patient_data(patient:Patients):
#     print(patient.name)   
#     print(patient.age)
    

# patients_info={'name':'suresh','age':"70"}
# patient1=Patients(**patients_info)
  
# insert_patient_data(patient1)  

# class Patient(BaseModel):
#     name:str
#     age:int
    
    
# def patients_get(patients:Patient):
#     print(patients.name)    
#     print(patients.age)    

# patients_info={"name":"john","age":30}
# patinets1=Patient(**patients_info)

# patients_get(patinets1)
#----------------------------------------------------
# class Patients(BaseModel):
#     # name:str =Field(max_length=7)
#     name:Annotated[str,Field(max_length=7,title="name of patient")]

#     email:EmailStr
#     URL:AnyUrl
#     age:int=Field(gt=0,lt=20)
#     weight:float=Field(gt=0)
#     married:bool=False
#     allergies:Optional[List[str]]=None
#     conatact_details:Dict[str,str]

# def patients_info(patient:Patients):
#     print(patient.name)    
#     print(patient.age)
#     print(patient.email)
#     print(patient.URL)    
#     print(patient.weight)
#     print(patient.married)
#     print(patient.allergies)
#     print(patient.conatact_details)
    
# patient_name={
#          "name":"satya",
#          "age":1,
#          "weight":1,
#          "URL":" h:e",
#          "email":"hello@gmail.com",
#          "married":True,
#          "allergies":["yes","yes"],
#          "conatact_details":{"email":"abc@gmail.com","phone":"98989"}}

# patient1=Patients(**patient_name)    
# patients_info(patient1)

#----------------------------------------------------
