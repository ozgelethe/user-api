from rest_framework import serializers
from .models import User

# this is gonna be inheriting from serializer
class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    
    class Meta:
        
        model=User
        # this is we want to expose. the password is gonna be right for me, 
        # it means that whenever we send back responses regarding this model
        # you will be saying there's anyone's email
        fields= ["email", "username", "password"]
        
    def validate(self, attrs):
        return super().validate(attrs)