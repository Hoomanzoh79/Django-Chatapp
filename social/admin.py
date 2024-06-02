from django.contrib import admin
from .models import Follow

@admin.register(Follow)
class RoomAdmin(admin.ModelAdmin):
    model = Follow
    list_display = ["follower","followed"]