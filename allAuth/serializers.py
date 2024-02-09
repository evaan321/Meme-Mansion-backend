from rest_framework import serializers

from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.views import APIView



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