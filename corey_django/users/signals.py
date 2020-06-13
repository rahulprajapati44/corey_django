# ravindra created to fire perticular action after saving something
from django.db.models.signals import post_save # to get post save signale
from django.contrib.auth.models import User
from django.dispatch import receiver # its a function which recieves that signal and performs some task we want
from .models import Profile # we will be creating profiles in our function so i imported it

# need to create profile for each new user

# post_save is signal which comes when user is saved , and it will be passed to our function create_profile

@receiver(post_save,sender =User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

# to save profile after creating it
@receiver(post_save,sender =User)
def save_profile(sender,instance,created,**kwargs):
    instance.profile.save()

# after creating this two signals we have to import it in users app apps.py file