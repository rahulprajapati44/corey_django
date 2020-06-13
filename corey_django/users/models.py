from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# creating profile model for each user

class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE) # if user is deleted then delete profile as well , using models.CASCADE
    image = models.ImageField(default='default.jpg', upload_to="profile_pics")

    def __str__(self):
        return  f'{self.user.username} Profile'