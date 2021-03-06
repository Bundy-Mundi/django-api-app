from rest_framework import serializers
from .models import User

class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "superhost") 

class UserSerializer(serializers.ModelSerializer):

    class Meta: 
        model = User
        fields = ("__all__")
