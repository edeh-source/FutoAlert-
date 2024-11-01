from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models  import update_last_login
from users.serializers import UserSerializer
from rest_framework_simplejwt.settings import api_settings



class UserRegisterSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True, format='hex')
    password = serializers.CharField(write_only=True, min_length=8)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    
    
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'image', 'first_name', 'phone_number','last_name', 'password', 'created', 'updated']