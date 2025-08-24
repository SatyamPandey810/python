from pydantic import BaseModel,EmailStr,computed_field
from typing import List,Dict

class Patients(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    height:float  
    married:bool
    allergies:List[str]
    conatact_details:Dict[str,str]   
    
    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi         
       
def patients_details(patient:Patients):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print("BMI -",patient.calculate_bmi)
    
    print(patient.married)
    print(patient.allergies)
    print(patient.conatact_details)

patient={'name':'shubham','email':"abc@gmail.com",'age':'70','weight':30.4,'height':1.98,
         'married':True,'allergies':['yes','no'],'conatact_details':{'emergency':'98989','email':'test@gmail.com'}
         }    
patient1=Patients(**patient)
patients_details(patient1)

    