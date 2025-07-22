from django.contrib import admin
from todo.models import Task
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display=('title','description')
    
 
admin.site.register(Task,TodoAdmin)    
