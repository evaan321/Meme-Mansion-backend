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
    username = serializers.CharField(source = 'user.username',read_only= True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    category = CategorySerializer(many= True ,)
    
    class Meta:
        model = Meme
        fields = ['username','user','title','photo','category',]
    
    
    
    