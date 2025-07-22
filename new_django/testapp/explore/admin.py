from django.contrib import admin
from explore.models import Explore


class ExploreAdmin(admin.ModelAdmin):
     list_display=('service_icon','service_title','service_heading','image','service_des')
     

admin.site.register(Explore,ExploreAdmin)
# Register your models here.
