from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['username','id']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = ['categoryName']


class MemeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    category = CategorySerializer(many= True ,read_only = True)
    class Meta:
        model = Meme
        fields = ['user','title','photo','category']
    

    
    