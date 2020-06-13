# ravindra created: this file is to create forms in user model

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

class UserRegisterForm(UserCreationForm): # inheriting user creation from to add extra feature like email address feild
    email = forms.EmailField(required=False) # given folse to make it not mandatory

    class Meta:
        model = User  # the form which will going to interact with is model= user
        fields = ['username','email','password1','password2'] # the fields which will be displayed

from django.db import models
# using this form we are allowing to update username and email
class UserUpdateForm(forms.ModelForm):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = forms.EmailField(required=False)  # given folse to make it not mandatory

    class Meta:
        model = User  # the form which will going to interact with is model= user
        fields = ['username', 'email']  # the fields which will be displayed

# profile update form allows to update image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile # model which we want to work with
        fields = ['image']