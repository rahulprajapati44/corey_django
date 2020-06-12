from django.db import models
from django.utils import timezone
# to get user models
from django.contrib.auth.models import User
# Create your models here.
# django supports orm-->  object relational mapper : it allows us to access to our database
# we will use sql lite db for testing
# we will use postgre db for production

# creating post model
class Post(models.Model):
    title = models.CharField(max_length=100) # title field will be of 100 characters
    content = models.TextField() # its unrestricted text
    date_posted= models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

