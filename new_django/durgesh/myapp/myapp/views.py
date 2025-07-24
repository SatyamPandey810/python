from django.shortcuts import render,redirect
from website.models import Student

# Create your views here.
def Home(request):
    student=Student.objects.all()
    return render(request,'index.html',{"employee":student})

def addEmp(request):
    if request.method == "POST":
        name=request.POST.get('name')
        emp_id=request.POST.get('emp_id')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        working=request.POST.get('working')
        department=request.POST.get('department') 
        
        e=Student()
        e.name=name
        e.emp_id=emp_id
        e.phone=phone
        e.address=address
        e.department=department
        if working is None:
           e.working=False  
        else:
            e.working =True 
        e.save()   
        # return redirect('add/')     

    return render(request,'addemp.html')

def deleteEmp(request,emp_id):
    st=Student.objects.get(id=emp_id)
    st.delete()
    return redirect('home')

def updateEmp(request,emp_id):
    st=Student.objects.get(id=emp_id)
    return render(request,'update.html',{"emp":st})

def do_updateEmp(request,emp_id):
    if request.method =='POST':
        name=request.POST.get('name')
        emp_id_temp=request.POST.get('emp_id')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        working=request.POST.get('working')
        department=request.POST.get('department') 
        
        e=Student.objects.get(id=emp_id)
        e.name=name
        e.emp_id=emp_id_temp
        e.phone=phone
        e.address=address
        e.department=department
        if working is None:
           e.working=False  
        else:
            e.working =True 
        e.save() 
        return redirect('home')
    # return redirect('update_emp', emp_id=emp_id)        
    