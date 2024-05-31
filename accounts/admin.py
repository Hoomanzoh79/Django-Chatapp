from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id','email', 'username','is_superuser','is_verified',)
    ordering = ['-id']
    list_editable = ['is_verified']

