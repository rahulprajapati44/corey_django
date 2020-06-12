from django.contrib import admin
from .models import Post
# Register your models here.

# we can register our models for admin page
admin.site.register(Post)  # we are registering Post model of blog app in admin page so we can access it functionality
# on admin page

