from django.db import models
from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class NewsApp(models.Model):
    title=models.CharField(max_length=200)
    description=HTMLField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)


    newSlug=AutoSlugField(populate_from='title',unique=True,null=True)
    def __str__(self):
        return self.title
    
