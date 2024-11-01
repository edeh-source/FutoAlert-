from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from posts.models import Post
import cv2
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.http import Http404



class UserManager(BaseUserManager):
    """
    A Blueprint to create a user
    """
    def get_object_by_id(self, id):
        try:
            instance = self.get(id=id)
            return instance
        except(ObjectDoesNotExist, ValueError, TypeError):
            return Http404
    
    
    def create_user(self, username, email, phone_number, password, **kwargs):
        """
        A Method to create a user from the blueprint
        """
        if username is None:
            raise ValidationError("User Must Have A Username")
        if email is None:
            raise ValidationError("User Must Have An Email")
        if phone_number is None:
            raise ValidationError("User Must Have A Phone Number")
        if password is None:
            raise ValidationError("User Must Have A Password")
        
        user = self.model(username=username, email=self.normalize_email(email), phone_number=phone_number, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, username, email, phone_number, password, **kwargs):
        """
        A method to create a superuser 
        """
        if username is None:
            raise ValidationError("SuperUser Must Have A Username")
        if email is None:
            raise ValidationError("SuperUser Must Have An Email")
        if phone_number is None:
            raise ValidationError("SuperUser Must Have A Phone Number")
        if password is None:
            raise ValidationError("SuperUser Must Have A Password")
        user = self.create_user(username=username, email=email, phone_number=phone_number, password=password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
    

    
    


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, unique=True, blank=False, editable=False, default=uuid.uuid4)
    username = models.CharField(max_length=256, db_index=True, unique=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256, db_index=True)
    image = models.ImageField(upload_to='users_images', blank=True)
    email = models.EmailField(max_length=256, unique=True, db_index=True)
    post_liked = models.ManyToManyField(Post, related_name='post_liked')
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='follow')
    phone_number = PhoneNumberField(blank=False, unique=True)
    bio = models.TextField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.email}"
    
    @property
    def name(self):
        return f"{self.first_name} {self.username}"
    
    
    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            image = cv2.imread(self.image.path)
            size = (100, 100)
            image = cv2.resize(image, size, interpolation=cv2.INTER_AREA)
            image_save = cv2.imwrite(self.image.path, image)
            return image_save
        else:
            pass
    
    def follow_user(self, user):
        """
        A method to allow or a follow a user
        """
        return self.followers.add(user)
    
    def unfollow_user(self, user):
        """
        A method to unfollow a user
        """
        return self.followers.remove(user)
    
    
    def user_follower_check(self, user):
        """
        A method to check if a user has followed another user
        """
        return self.followers.filter(pk=user.pk).exists()
    
    
        
    
    
    
    def like_post(self, post):
        """
        A method to like a given post
        """
        return self.post_liked.add(post)
    
    
    def unlike_post(self, post):
        """
        A Method To Unlike A Post
        """
        return self.post_liked.remove(post)
    
    def post_like_check(self, post):
        """
        A Method to check if a post have been liked by a user
        """
        return self.post_liked.filter(pk=post.pk).exists()
        
            
    
    
    
    objects = UserManager()
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'username']
    
    
    
    
    