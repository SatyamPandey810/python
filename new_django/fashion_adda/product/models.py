from django.db import models
from base.models import BaseModel
from django.utils.text import slugify

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug=models.SlugField(unique=True,null=True,blank=True)

    def save(self,*args ,**kwargs):
        self.slug=slugify(self.category_name)   
        super(Category,self).save(*args ,**kwargs)

    def __str__(self):
        return self.category_name
class SubCategory(BaseModel):
    subcategory_name = models.CharField(max_length=100)
    slug=models.SlugField(unique=True,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="subcategory")
    SubCategory_image=models.ImageField(upload_to='images/', null=True,blank=True)

    def save(self,*args ,**kwargs):
        if not self.slug:
            self.slug = slugify(self.subcategory_name)
            base_slug = self.slug
            counter = 1
            while SubCategory.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.subcategory_name  
  

class ColorVariant(BaseModel):
    color_name=models.CharField(max_length=100)
    prise=models.IntegerField(default=0)
  
    def __str__(self):
        return self.color_name 
  
  
class SizeVatiant(BaseModel):  
    size_name=models.CharField(max_length=100)
    prise=models.IntegerField(default=0)
    
    def __str__(self):
        return self.size_name
    
  
class Product(BaseModel):
    product_name=models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    slug=models.SlugField(unique=True,null=True,blank=True)
    produt_image=models.ImageField(upload_to='images/',null=True,blank=True)
    price=models.IntegerField()
    product_description=models.TextField()
    color_variant=models.ManyToManyField(ColorVariant,blank=True)
    size_variant=models.ManyToManyField(SizeVatiant,blank=True)
    
    
    def save(self,*args ,**kwargs):
        self.slug=slugify(self.product_name)
        super(Product,self).save(*args ,**kwargs)

    def __str__(self):
        return self.product_name  
    
    def get_product_price_by_size(self,size):
        return self.price + SizeVatiant.objects.get(size_name=size).price
        

class ProductImage(BaseModel):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_images")    
    image=models.ImageField(upload_to='images/', null=True, blank=True)

    
