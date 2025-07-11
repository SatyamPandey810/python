from django.contrib import admin
from .models import ChaiVaity,ChaiReview,Store,ChaiReview,ChaiCertificate


# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type',)
    inlines = [ChaiReviewInline]
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display=('chai',"certificate_number")


admin.site.register(ChaiVaity,ChaiVarietyAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(ChaiReview)
admin.site.register(ChaiCertificate,ChaiCertificateAdmin)





