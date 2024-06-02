from django.db import models
from django.contrib.auth import get_user_model


class Follow(models.Model):
    follower = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="follower")

    followed = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="followed")

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower} follows {self.following}"

