from pydantic import BaseModel,EmailStr,model_validator
from typing import List,Dict,Optional,Annotated

class Patients(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    conatact_details:Dict[str,str]   
    
    @model_validator(mode='after')
    def validate_eme_contact(cls,model):
        if model.age>60 and 'emergency' not in model.conatact_details:
            raise ValueError('Patients older than 60 must have an emergency number')
        return model
    
    
def patients_details(patient:Patients):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.conatact_details)

patient={'name':'shubham','email':"abc@gmail.com",'age':'70','weight':30.4,
         'married':True,'allergies':['yes','no'],'conatact_details':{'emergency':'98989','email':'test@gmail.com'}
         }    
patient1=Patients(**patient)
patients_details(patient1)

    