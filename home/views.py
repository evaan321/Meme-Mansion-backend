from django.shortcuts import render
from .models import *
from .serializers import *
# Create your views here.
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser

class Memereg(viewsets.ModelViewSet):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
    parser_classes = [MultiPartParser]

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()  
    serializer_class = CategorySerializer

class Memeview(viewsets.ModelViewSet):
    queryset = Meme.objects.all()
    serializer_class = MemSerializer
    parser_classes = [MultiPartParser]


