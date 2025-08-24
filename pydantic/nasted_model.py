from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address
    
    
address_dict={'city':'noida','state':'UP','pin':'23232'}    
address1=Address(**address_dict)
patients_dict={'name':'john','gender':'male','age':30,'address':address1}
patient1=Patient(**patients_dict)


print(patient1)
print(patient1.name)
print(patient1.address.pin)




temp=patient1.model_dump(include=['name'])   # exclude
# temp=patient1.model_dump_json()


print(temp)
# print(type(temp))
# print(type(temp))


