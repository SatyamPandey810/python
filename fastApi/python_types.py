from fastapi import FastAPI
app=FastAPI
def full_name(fname,lname):
    return fname.capitalize()+" " +lname

print(full_name('john','doe'))