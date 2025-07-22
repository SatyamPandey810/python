from django.shortcuts import render
from app.models import NewsApp

def homePage(request):
    newsData=NewsApp.objects.all()
    
    if request.method=="GET":
        st=request.GET.get("search")
        if st != None:
         newsData=NewsApp.objects.filter(title__icontains=st)
         
         
        
    return render(request,"index.html",{"newsdata":newsData})

def detialsPage(request,slug):
    newsDetails=NewsApp.objects.get(newSlug=slug)
    return render(request,'details.html',{'details':newsDetails})   