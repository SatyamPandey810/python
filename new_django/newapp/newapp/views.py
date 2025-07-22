from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    data = {
        'title':'Home Page',
        'mydata':'Home page is awesome',
        'clist':['MERN','PYTHON','DJANGO'],
        'numbers':[10,20,30,40],
        'student_details':[
            {'name':'Rajkumar','phone':1234567},
            {'name':'Deepak','phone':7654321},
        ]
    }

    return render(request,'index.html',data)   # Render the HTML file


def aboutUs():
    return HttpResponse("Welcome to About page")

def contact():
    return HttpResponse("welocome to contacts page")    

def courceDetails(courseid):      # dynamic route
    return HttpResponse(courseid)
