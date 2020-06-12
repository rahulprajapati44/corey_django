from django.contrib import admin

# Register your models here.

from .models import Profile

# registering my created Profile model(models.py) for admin
admin.site.register(Profile)

