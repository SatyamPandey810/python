from django.contrib import admin
from app.models import NewsApp

class NewsAdmin(admin.ModelAdmin):
    list_display=('title','description','image')
    
admin.site.register(NewsApp,NewsAdmin)    


