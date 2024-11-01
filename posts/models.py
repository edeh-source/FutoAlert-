from django.db import models
import uuid
from django.conf import settings
import cv2



class Post(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, blank=False, default=uuid.uuid4, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()
    image = models.ImageField(upload_to='posts_images', blank=True)
    edited = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.author.name
    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            image = cv2.imread(self.image.path)
            size = (300, 600)
            image = cv2.resize(image, size, interpolation=cv2.INTER_AREA)
            post_images = cv2.imwrite(self.image.path, image)
            return post_images
        else:
            pass
    
    