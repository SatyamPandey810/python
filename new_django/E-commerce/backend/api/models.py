from django.db import models
from django.conf import settings
from tinymce.models import HTMLField


class banners(models.Model):
    bannerTitle=models.CharField(max_length=400)
    bannerDis=HTMLField()
    bannerImg=models.ImageField(upload_to='images/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    
class NewProduct(models.Model):
    productName=models.CharField(max_length=200)    
    productPrice=models.DecimalField(max_digits=10,decimal_places=2)
    is_active=models.BooleanField(default=True)
    
    
def  __str__(self):
    return self.bannerTitle

# Create your models here.
