from rest_framework import serializers
from users.models import User
from .models import Reply
from comments.models import Comment
from django.core.exceptions import ValidationError




class ReplySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    comment = serializers.SlugRelatedField(queryset=Comment.objects.all(), slug_field='id')
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='id')
    edited = serializers.BooleanField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    
    
    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You Can Not Reply For Another User")
        return value
    
    
    
    
    
    class Meta:
        model = Reply
        fields = ['id', 'comment', 'author', 'text', 'created', 'updated', 'edited',]