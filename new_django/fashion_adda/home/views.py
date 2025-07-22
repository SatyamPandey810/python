from django.shortcuts import render
from product.models import Category

def home(request):   
    categories = Category.objects.prefetch_related('subcategory__product_set').all()
    
    return render(request,'index.html',{'categories':categories })
