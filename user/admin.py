from django.contrib import admin
from django.contrib.auth.models import Group

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel

# Register your models here.

#unregister group model
admin.site.unregister(Group)

class UserAdmin(admin.ModelAdmin):
    search_fields: ('fullname')

class HobbyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

# admin.py
admin.site.register(UserModel, UserAdmin)
admin.site.register(UserProfileModel)
admin.site.register(HobbyModel, HobbyAdmin)