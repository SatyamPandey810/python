from django.shortcuts import render,redirect
from todo.models import Task
from django.contrib import messages

def homePage(request):
    if request.method == 'POST':
        title=request.POST.get('title','')
        description=request.POST.get('description','')
        print(request.Post)
        if title and description:
            Task.objects.create(title=title,description=description)
            messages.success(request,'Task added successfully....')
                      
        else:
          messages.error(request, ' Please provide both title and description.')
  

        return redirect('/')    
    task=Task.objects.all()
    return render(request,'index.html',{'task':task})