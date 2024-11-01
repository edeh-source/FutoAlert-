from django.db import models
import uuid
from posts.models import Post
from users.models import User


class Comment(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, blank=False, editable=False, db_index=True, default=uuid.uuid4)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    edited = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.author} comment on {self.post}"
    