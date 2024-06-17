from django.contrib import admin
from .models import Room,Message

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    model = Room
    list_display = ["name","user1","user2"]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ["room","content","author","datetime"]