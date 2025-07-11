from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world i am home page")
    return render(request,'index.html')

def about(request):
    return HttpResponse("Hello world i am about page")

def contact(request):
    return HttpResponse("Hello world i am contact")
