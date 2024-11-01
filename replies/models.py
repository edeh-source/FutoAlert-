from django.db import models
from comments.models import Comment
import uuid

from users.models import User



class Reply(models.Model):
    id = models.UUIDField(primary_key=True, db_index=True, unique=True, editable=False, blank=False, default=uuid.uuid4)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies')
    text = models.TextField()
    active = models.BooleanField(default=True)
    edited = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.author}'s reply on {self.comment}"
    
    
    
    
