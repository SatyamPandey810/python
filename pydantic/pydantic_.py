
# def insert_petient_data(name,age):    
#     if type(name)==str and type(age)==int:        
#      print(name)
#      print(age)
#     else:
#         print("somthing went wrong")  

# insert_petient_data('john',"12")

from pydantic import BaseModel
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

