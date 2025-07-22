from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import UsersForm
from explore.models import Explore
from django.conf.urls.static import static


# def homePage(request):
#   return  HttpResponse("hello world")

# def prodctPage(request,product):
#     return HttpResponse(product)

def home(request):
    serviceData=Explore.objects.all().order_by('service_title')[:4]
    return render(request,'index.html',{'a':serviceData})

def aboutUs(request):
  if  request.method =="GET":
      output=request.GET.get('output')
  return render(request,'about.html',{'output':output})

def contactUs(request):
     finalres=0 
     data={}
     try:
        if request.method=='POST': 
        # name1=int(request.POST['n1'])
        # email1=int(request.POST['n2'])
         name1=int(request.POST.get('n1'))
         email1=int(request.POST.get('n2'))        
         finalres=name1+email1
         data={
             'n1':name1,
             'n2':email1,
             'output':finalres
         }
         url="/about/?output={}".format(finalres)
         return HttpResponseRedirect(url)
     except:
        pass  
     return render(request,'contact.html',
                    data
                #    {'output':finalres}
                   )
def submited(request):
    return HttpResponse("thanku")

def services(request):         
    return render(request,'service.html')

def team(request):
    return render(request,'team.html')

def testmonial(request):
    return render(request,'testimonial.html')
    
def booking(request):
    return render(request,'booking.html')

def pageNotFound(request):
    return render(request,'404.html')

# def calculator(request):
#     c=''
#     num1 = ''
#     num2 = ''
#     opr = ''

#     try:
#         if request.method=="POST":
#             n1 = request.POST.get("num1")
#             n2 = request.POST.get("num2")
#             opr = request.POST.get("opr")
            
#             n1 = float(num1)
#             n2 = float(num2)
#             if opr == "+":
#                 c=n1+n2
#             elif opr == "-": 
#                 c=n1-n2
#             elif opr == "*":
#                 c=n1*n2
#             elif opr == "/":
#                 c=n1/n2   
#             elif opr == "%":
#                 c=n1%n2     
#     except:    
#         c="Invalid crediantional"
#     print(c)
        
#     return render(request,'calculator.html',{'c': c,
#         'num1': num1,
#         'num2': num2,
#         'opr': opr})

def calculator(request):
    c = ''
    num1 = ''
    num2 = ''
    opr = ''

    try:
        if request.method == "POST":
            num1 = request.POST.get("num1")
            num2 = request.POST.get("num2")
            opr = request.POST.get("opr")

            # Convert to float or int
            n1 = float(num1)
            n2 = float(num2)

            # Perform operations safely
            if opr == "+":
                c = n1 + n2
            elif opr == "-":
                c = n1 - n2
            elif opr == "*":
                c = n1 * n2
            elif opr == "/":
                c = n1 / n2 if n2 != 0 else "Cannot divide by zero"
            elif opr == "%":
                c = n1 % n2
            else:
                c = "Invalid operator"
    except ValueError:
        c = "Please enter valid numbers"
    except Exception as e:
        c = "Error: " + str(e)

    return render(request, 'calculator.html', {
        'c': c,
        'num1': num1,
        'num2': num2,
        'opr': opr
    })
    
    
# if settings.DEBUG:
#  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    