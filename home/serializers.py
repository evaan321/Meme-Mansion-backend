from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['username']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = '__all__'




class MemeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source = 'user.username',read_only= True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    

    
   
    
    class Meta:
        model = Meme
        fields = ['username','user','title','photo','category',]
    
    

class MemSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source = 'user.username',read_only= True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    

    
   
    
    class Meta:
        model = Meme
        fields = ['username','user','title','photo','category',]
        depth = 1