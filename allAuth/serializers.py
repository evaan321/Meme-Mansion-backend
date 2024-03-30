from rest_framework import serializers

from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .models import *


class RegisterationSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username','email','password','confirm_password']

    def save(self):
        username = self.validated_data['username']
        # first_name = self.validated_data['first_name']
        # last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password :
            raise serializers.ValidationError({'error' : "password doesn't match"})
        
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'error': 'Email Already Exist'})
        account = User(username = username , email = email )
        account.set_password(password)
        account.is_active = False
        account.save()
        return account
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)

class UserUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserUpdateSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

    def update(self, instance, validated_data):
        

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)

       
        

        
        instance.save()
       

        return instance
    

class userserializer(serializers.ModelSerializer):
    
    class Meta:
        model  = User
        fields = ['id', 'email', 'username', 'first_name','last_name']


class profileserializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id',read_only = True)
    email = serializers.EmailField(source='user.email',read_only = True)
    username = serializers.CharField(source='user.username',read_only = True)
    class Meta:
        model  = UserProfile
        fields = ['user_id', 'email', 'username', 'bio', 'avater']