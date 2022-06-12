from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Products

# Create your views here.

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

