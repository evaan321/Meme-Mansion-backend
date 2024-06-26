from django.shortcuts import render,redirect

from rest_framework import viewsets,response

from .models import *

from .serializers import *

from rest_framework.views import APIView,Response

from django.contrib.auth.tokens import default_token_generator

from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode

from django.utils.encoding import force_bytes

from rest_framework.parsers import MultiPartParser

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout
from rest_framework import generics


class UserRegistrationApiView(APIView):
    serializer_class = RegisterationSerializer

    def post(self,request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            confirm_link = f'https://meme-mansion-backend.onrender.com/active/{uid}/{token}'
            email_subject = "Confirm Your Email"
            
            email = EmailMultiAlternatives(email_subject, f'Click this link to confirm {confirm_link}',to=[user.email])
            email.send()
            return Response('Check mail for Confirmation')
        return Response(serializer.errors)


def activate(request,token,uid64):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk = uid)
    except(User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('login')
    
    else:
        return redirect('register')

class UserLoginApiView(APIView):
    def post(self , request):
        serializer = UserLoginSerializer(data = self.request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username = username , password = password)

            if user:
                token , _ = Token.objects.get_or_create(user = user)
                login(request,user)
                return Response({'token' : str(token) , 'user_id': user.id})
            else:
                return Response({'error': 'Invalid Credintials'})
        
        return Response (serializer.errors)
    
class UserLogoutView(APIView):
    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')


   
class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    
    def get_object(self):
        return self.request.user
    
class profileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = profileserializer
    parser_classes = [MultiPartParser]


class userView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userserializer
    

  