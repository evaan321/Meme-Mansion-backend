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
        fields = ['categoryName']


class MemeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer(many= True)
    class Meta:
        model = Meme
        fields = '__all__'