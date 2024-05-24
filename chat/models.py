from django.db import models
from django.contrib.auth import get_user_model

class Room(models.Model):
    name = models.CharField(max_length=30,)
    online = models.ManyToManyField(get_user_model(),blank=True)

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return f'{self.name} : ({self.get_online_count()})'


class Message(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username}: {self.content}'