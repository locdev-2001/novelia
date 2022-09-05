from django.db import models
from django.contrib.auth import get_user_model
import uuid
User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profileImg = models.ImageField(upload_to='avatar', default='blank-profile-picture.png')
    firstName = models.CharField(max_length=100, blank=True)
    lastName = models.CharField(max_length=100, blank=True)
    gender = models.BooleanField(default=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='post_img')
    caption = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    liked  = models.IntegerField(default=0)
    
    def __str__(self):
        return  self.user