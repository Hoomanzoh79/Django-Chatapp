from django.db import models
from django.contrib.auth import get_user_model


class Room(models.Model):
    user1 = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.SET_NULL, related_name="user1"
    )
    user2 = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.SET_NULL, related_name="user2"
    )
    name = models.CharField(max_length=100, unique=True)

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return f"{self.name}"


class Message(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}: {self.content} time: {self.datetime}"
