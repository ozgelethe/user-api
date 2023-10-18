from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RegisterSerializer
from rest_framework.response import Response

# Create your views here.

class RegisterView(generics.GenericAPIView):
    
    serializer_class = RegisterSerializer
    
    def post(self, request):
        
        user = request.data
        
        # this will send the data to serializer
        serializer = self.serializer_class(data=user)
        
        # this is gonna run a method called validate
        serializer.is_valid(raise_exception=True)
        
        # this is gonna run a method called create
        serializer.save()
        
        user_data = serializer.data
        
        return Response(user_data, status=status.HTTP_201_CREATED)