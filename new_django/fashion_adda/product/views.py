from django.shortcuts import render
from product.models import Product

def get_product(request,slug):
    try:
        product= Product.objects.get(slug=slug)
        return render(request,'product-details.html' ,{'product':product})

    except Exception as e:
        print(e)  
    
