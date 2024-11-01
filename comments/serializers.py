from posts.models import Post
from rest_framework import serializers
from users.models import User
from .models import Comment
from django.core.exceptions import ValidationError




class CommentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True, format='hex')
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='id')
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='id')
    edited = serializers.BooleanField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    replies_count = serializers.SerializerMethodField()
    updated = serializers.DateTimeField(read_only=True)
    
    
    def get_replies_count(self, instance):
        return instance.comments.count()
    

    
    def validate_author(self,  value):
        if self.context["request"].user != value:
            raise ValidationError("You Can Not Comment For Another User")
        return value
    
    
    
    
    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'replies_count', 'edited', 'text','created', 'updated']