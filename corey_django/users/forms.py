from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm): # inheriting user creation from to add extra feature like email address feild
    email = forms.EmailField(required=False) # given folse to make it not mandatory

    class Meta:
        model = User  # the form which will going to interact with is model= user
        fields = ['username','email','password1','password2'] # the fields which will be displayed