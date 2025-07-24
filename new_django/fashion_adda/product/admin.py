from django.contrib import admin

from .models import *

admin.site.register(Category) 
admin.site.register(SubCategory)    
# admin.site.register(Product) 
admin.site.register(ProductImage) 

class ProductAdmin(admin.ModelAdmin):
    list_display=["product_name",'category','subcategory','price']

admin.site.register(Product,ProductAdmin)    

@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display=['color_name','prise']
    model=ColorVariant
  
@admin.register(SizeVatiant)    
class SizeVariantAdmin(admin.ModelAdmin):
    list_display=['size_name','prise']
    models=SizeVatiant    
    
    

    
   
   
