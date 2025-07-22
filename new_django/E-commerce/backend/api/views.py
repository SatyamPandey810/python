from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from api.models import banners
from api.serializers import BannerSerializer

class BannerViewSet(viewsets.ModelViewSet):
    queryset=banners.objects.all()
    serializer_class=BannerSerializer