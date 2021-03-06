from django.contrib import admin
from django.contrib.auth.models import Group

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#unregister group model
admin.site.unregister(Group)

# Register your models here.
# class UserProfileInline(admin.TabularInline): # 가로로 뿌려줌
class UserProfileInline(admin.StackedInline): # 세로로 뿌려줌
    model = UserProfileModel


    # def formfield_for_manytomany(self, db_field, request, **kwargs): # 내가 원하는 필드에서 보여주고 싶은 것만 보여주게 예외처리하기 / 폼필드 설정
    #     if db_field.name == 'hobby':
    #         kwargs['queryset'] = HobbyModel.objects.filter(id__lte=7)

    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

 # UserAdmin 상속받으면 list_display, list_display_links, list_filter, filter_horizontal = [] 들이 필수 값이다.
class UserAdmin(BaseUserAdmin):
    filter_horizontal = []
    list_display = ('id', 'username', 'fullname')
    list_display_links = ('id', 'username', )
    list_filter = ('fullname', )
    search_fields = ('username', )
    readonly_fields = ('username', 'join_date', )

    fieldsets = (
        ("info", {'fields': ('username', "password", 'fullname', 'join_date')}),
        ('permissions', {'fields': ('is_admin', 'is_active', )}),
    )

    inlines = (
            UserProfileInline,
        )

    # def has_add_permission(self, request, obj=None): # 추가 권한
    #     return False

    # def has_delete_permission(self, request, obj=None): # 삭제 권한
    #     return False

    # def has_change_permission(self, request, obj=None): # 수정 권한
    #     return False
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

# admin.py
admin.site.register(UserModel, UserAdmin)
# admin.site.register(UserProfileModel)
admin.site.register(HobbyModel, HobbyAdmin)