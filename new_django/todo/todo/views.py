from django.shortcuts import render,redirect,get_object_or_404
from service.models import Task
from django.contrib import messages

def homePage(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        
        if title and description:
            Task.objects.create(title= title,description=description)
            return redirect('home')
        else :
            print("Somthing went wrong")
   
            
            
    tasks = Task.objects.all()[:5]
    if request.method=="GET":
        st=request.GET.get('search')
        if st != None:
            tasks=Task.objects.filter(title__icontains=st)        
             
    return render(request,'index.html',{'tasks':tasks}) 


def delete_task(request,task_id):
   try:
        task = Task.objects.get(id=task_id)
        task.delete()
   except Task.DoesNotExist:
        print(f"Task with ID {task_id} not found")
   return redirect('home')

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('task_list')  # Replace with your task list URL name
    return render(request, 'home', {'task': task})