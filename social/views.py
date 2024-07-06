from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import CustomUser
from .models import Follow, Post, Comment
from .forms import PostForm, CommentForm


class SearchResultsView(generic.ListView):
    model = get_user_model()
    template_name = "social/search_results.html"
    context_object_name = "users"

    def get_queryset(self):  # new
        search_query = self.request.GET.get("q")
        if not search_query:
            search_query = ""
        object_list = self.model.objects.filter(username__icontains=search_query)
        return object_list

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        search_query = self.request.GET.get("q")
        context.update(
            {
                "search_query": search_query,
            }
        )
        return context


def follow(request, username, option):
    user = request.user
    following = get_object_or_404(get_user_model(), username=username)
    try:
        f, created = Follow.objects.get_or_create(follower=user, following=following)

        if int(option) == 0:
            f.delete()
            messages.warning(request, "successfully unfollowed this user")
        else:
            messages.success(request, "successfully followed this user")

        return HttpResponseRedirect(
            reverse("accounts:account-detail", kwargs={"slug": username})
        )

    except CustomUser.DoesNotExist:
        return HttpResponseRedirect(
            reverse("accounts:account-detail", kwargs={"slug": username})
        )


def like(request, pk, option):
    user = request.user
    post = get_object_or_404(Post, id=pk)

    if int(option) == 0:
        post.likes.remove(user)
    else:
        post.likes.add(user)

    return redirect(post.get_absolute_url())


class FollowersList(generic.ListView):
    template_name = "social/followers_list.html"
    context_object_name = "follows"
    pk_url_kwarg = "username"

    def get_queryset(self, **kwargs):
        user = get_object_or_404(get_user_model(), username=self.kwargs["username"])
        follows = Follow.objects.select_related("following", "follower").filter(
            following=user
        )
        return follows


class FollowingsList(generic.ListView):
    template_name = "social/following_list.html"
    context_object_name = "follows"
    pk_url_kwarg = "username"

    def get_queryset(self, **kwargs):
        user = get_object_or_404(get_user_model(), username=self.kwargs["username"])
        follows = Follow.objects.select_related("following", "follower").filter(
            follower=user
        )
        return follows


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = "social/post_create.html"

    def form_valid(self, form):
        self.author = self.request.user
        form.instance.author = self.author
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("accounts:account-detail", kwargs={"slug": self.author.username})


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "social/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post_id = self.kwargs["pk"]
        post = get_object_or_404(Post, id=post_id)
        user = self.request.user
        # like counts
        like_counts = post.likes.count()
        # check if user already liked the post or not
        like_status = False
        if user in post.likes.all():
            like_status = True
        # comments
        connected_comments = post.comments.all()
        number_of_comments = connected_comments.count()
        context.update(
            {
                "like_status": like_status,
                "like_counts": like_counts,
                "comments": connected_comments,
                "number_of_comments": number_of_comments,
                "comment_form": CommentForm(),
            }
        )
        return context


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    redirect_field_name = ""

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        post_id = self.kwargs.get("pk")
        post = get_object_or_404(Post, id=post_id)
        obj.post = post

        try:
            parent = form.cleaned_data["parent"]
        except:
            parent = None
        obj.parent = parent

        messages.success(self.request, "You wrote a comment on this post")

        return super().form_valid(form)
