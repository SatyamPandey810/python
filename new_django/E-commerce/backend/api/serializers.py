from rest_framework import serializers
from .models import banners

class BannerSerializer(serializers.ModelSerializer):
    bannerImg=serializers.ImageField(max_length=None,use_url=True)


    class Meta:
       model=banners
       fields=['id','bannerTitle','bannerDis','bannerImg','is_active']

