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
        
        # this checks for email, gets the email and puts fallback, 
        # so it doesnt crash
        email = attrs.get("email", "")
        
        username = attrs.get("username", "")
        
        if not username.isalnum():
            raise serializers.ValidationError("username should only contain letters.")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)