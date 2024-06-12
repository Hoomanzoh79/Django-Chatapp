from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse("social:post-detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE , related_name='replies')

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.post}: {self.body}'

    def get_absolute_url(self):
        return reverse("social:post-detail", kwargs={"pk": self.post.pk})
    
    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False