from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated
class Patients(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    conatact_details:Dict[str,str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domain=['hdfc.com','sbi.com']
        domain_name=value.split('@')[-1]
        
        if domain_name not in valid_domain:
            raise ValueError("not valid domain")
        return value
    
    @field_validator('name')    
    @classmethod
    def tranfom_name(cls,value):
       return value.upper()
   
    @field_validator('age',mode='after') #-> before
    @classmethod
    def validate_age(cls,value):
        if 0<value <100:
            return value
        else:
            raise ValueError("Age should be in between 0 and 100")
   
        

def patients_info(patient:Patients):
    print(patient.name)    
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.conatact_details)
    
patient_name={
         "name":"satya",
         "email":"hello@hdfc.com",
         "age":"20",
         "weight":1,
         "married":True,
         "allergies":["yes","yes"],
         "conatact_details":{"email":"abc@sbi.com","phone":"98989"}}

patient1=Patients(**patient_name)    
patients_info(patient1)