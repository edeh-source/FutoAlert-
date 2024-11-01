from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    post_likes = serializers.SerializerMethodField()
    user_followers = serializers.SerializerMethodField()
    
    
    
    
    
    def get_post_likes(self, instance):
        return instance.post_liked.count()
    
    def get_user_followers(self, instance):
        return instance.followers.count()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'user_followers', 'first_name', 'last_name', 'post_likes', 'is_active', 'created', 'updated', 'image']