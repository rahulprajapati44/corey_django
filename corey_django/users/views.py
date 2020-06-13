from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
# to desplay messages on form submiting
from django.contrib import messages

# to make necessary login, user must be login to view this page
from django.contrib.auth.decorators import login_required

# importing our created form which is inherited from usercreationform to add email field
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)  #<-we are giving instance of current working user by providing
        # request.user in to our UserForm
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)#<-we are giving profile instance of current working user
        # by providing  request.user.profile in to our ProfileUpdateForm
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile is updated!!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)  # <-we are giving instance of current working user by providing
        # request.user in to our UserForm
        p_form = ProfileUpdateForm(
            instance=request.user.profile)  # <-we are giving profile instance of current working user
        # by providing  request.user.profile in to our ProfileUpdateForm
    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request,"users/profile.html", context)

