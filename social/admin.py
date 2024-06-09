from django.contrib import admin
from .models import Follow,Post

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    model = Follow
    list_display = ["follower","following","follow_date"]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ["id","author"]