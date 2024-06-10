from django.db import models
from django.contrib.auth import get_user_model


class Follow(models.Model):
    follower = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="follower")

    following = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="following")

    follow_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower} follows {self.following}"



class Post(models.Model):
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    caption = models.TextField()
    likes = models.ManyToManyField(get_user_model(),related_name="likes",blank=True)
    picture = models.ImageField(upload_to='social/post_pictures')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)