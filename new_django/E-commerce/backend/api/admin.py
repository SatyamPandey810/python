from django.contrib import admin
from api.models import banners

class BannerAdmin(admin.ModelAdmin):
    list_display=('bannerTitle','bannerDis','bannerImg','is_active')
    
admin.site.register(banners,BannerAdmin)    
    
