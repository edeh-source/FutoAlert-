from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.serializers import UserSerializer
from .models import Post
from django.core.exceptions import ValidationError



class PostSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True, format='hex')
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='id')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    comment_count = serializers.SerializerMethodField()
    liked = serializers.SerializerMethodField()
    post_liked = serializers.SerializerMethodField()
    active = serializers.BooleanField(read_only=True)
    edited = serializers.BooleanField(read_only=True)
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_id(rep["author"])
        rep["author"] = UserSerializer(author).data
        return rep
    
    def get_liked(self, instance):
        request = self.context.get('request', None)
        if request is None or request.user.is_anonymous:
            return False
        return request.user.post_like_check(instance)
    
    
    
    
    
    def get_comment_count(self, instance):
        return instance.posts.count()
    
    def get_post_liked(self, instance):
        return instance.post_liked.count()
    
    
    
    
    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You Can Not Create A Post For Another User")
        return value
    
    def update(self, instance, validated_data):
        print("This is the instance", instance)
        if not instance.edited:
            validated_data["edited"] = True
        instance = super().update(instance, validated_data)
        return instance    
    
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'created', 'updated', 'comment_count', 'post_liked', 'liked','text', 'active', 'image','edited']