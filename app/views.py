from django.shortcuts import render
from .models import User
from rest_framework.response import Response
from rest_framework import generics
from .serializers import UserSerializer

class LoginView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
