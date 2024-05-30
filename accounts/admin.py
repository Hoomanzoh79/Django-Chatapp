from django.contrib import admin
from .models import CustomUser,Profile
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id','email', 'username','is_superuser','is_verified',)
    ordering = ['-id']
    list_editable = ['is_verified']
    list_per_page = 10

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('id','user','first_name','last_name','phone_number','email')
    ordering = ['-id']
    list_per_page = 10
    search_fields = ['user']
    list_filter = ['datetime_created']