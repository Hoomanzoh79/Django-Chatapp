from django.forms import ModelForm

from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["picture", "caption"]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body", "parent"]
