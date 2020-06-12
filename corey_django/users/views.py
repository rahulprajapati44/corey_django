from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
# to desplay messages on form submiting
from django.contrib import messages

# to make necessary login, user must be login to view this page
from django.contrib.auth.decorators import login_required

# importing our created form which is inherited from usercreationform to add email field
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # We are validating
        if form.is_valid():
            form.save() # to save form data in database
            username = form.cleaned_data.get('username')
            #email = form.cleaned_data.get('email')
            messages.success(request, 'Your account has been created! You can  log in now')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form})


@login_required
def profile(request):
    return render(request,"users/profile.html")