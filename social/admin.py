from django.contrib import admin
from .models import Follow,Post,Comment

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    model = Follow
    list_display = ["follower","following","follow_date"]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ["id","author"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['id','post', 'author', 'active','body','datetime_created','parent']