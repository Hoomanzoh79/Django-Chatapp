from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        "email",
        "username",
        "first_name",
        "last_name",
        "phone_number",
        "is_superuser",
        "is_verified",
    ]
    list_editable = ["is_verified"]
    add_form = CustomUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("phone_number", "profile_picture")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("phone_number", "profile_picture")}),
    )
