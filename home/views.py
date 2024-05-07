from django.shortcuts import render
from .models import *
from .serializers import *
# Create your views here.
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json

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

@api_view(['POST'])

def like_meme(request, meme_id):
    # Retrieve user ID from the request body
    data = json.loads(request.body)
    user_id = data.get('userId')
    
    # Fetch the meme object
    meme = get_object_or_404(Meme, pk=meme_id)
    
    # Add user ID to meme likes
    meme.likes.add(user_id)

    return JsonResponse({'message': 'Meme liked successfully'}, status=200)

def myfunc(s):
    ab = 's'
    