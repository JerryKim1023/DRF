from django.contrib import admin

from .models import Hobby, User, UserProfile

# Register your models here.

# admin.py
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Hobby)