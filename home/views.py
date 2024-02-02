from django.shortcuts import render
from .models import *
from .serializers import *
# Create your views here.
from rest_framework import viewsets


class Memeview(viewsets.ModelViewSet):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
