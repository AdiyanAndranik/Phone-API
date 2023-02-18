from django.shortcuts import render
from .serializers import PhoneSerializer, CategorySerializer
from .models import Phone, Category
from rest_framework import viewsets

class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PhoneViewSets(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer