from django.db import models


class Explore(models.Model):
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=100)
    service_heading=models.CharField(max_length=100)
    image = models.ImageField(upload_to='explore_images/', null=True, blank=True)
    service_des = models.TextField()
 

# Create your models here.
