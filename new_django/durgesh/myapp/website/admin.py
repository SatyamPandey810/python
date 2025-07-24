from django.contrib import admin
from .models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','emp_id','phone','address','working','department']
    

admin.site.register(Student,StudentAdmin)


