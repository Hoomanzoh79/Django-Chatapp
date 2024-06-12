from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages

from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser
from social.models import Follow,Post


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")


class EditAccountView(LoginRequiredMixin,generic.UpdateView):
    form_class = CustomUserChangeForm
    template_name = "accounts/edit_account.html"
    success_url = reverse_lazy("accounts:edit-account")


    def get_object(self):
        username = self.request.user.username
        account = get_object_or_404(CustomUser,username=username)
        return account

    def form_valid(self, form):
        messages.success(self.request,"successfully changed your profile")
        return super().form_valid(form)


class AccountDetailView(LoginRequiredMixin,generic.DetailView):
    model = CustomUser
    template_name = "accounts/account_detail.html"
    context_object_name = "account"
    slug_field = "username"

    def get_context_data(self, **kwargs):
        context = super(AccountDetailView, self).get_context_data(**kwargs)
        follower_user = self.request.user
        username = self.kwargs['slug']
        following_user = get_object_or_404(get_user_model(),username=username)
        # follow status
        follow_status = Follow.objects.filter(following=following_user,follower=follower_user).exists()
        
        # profile stats
        followings_count = Follow.objects.filter(follower=following_user).count()
        followers_count = Follow.objects.filter(following=following_user).count()
        # profile posts
        posts = Post.objects.filter(author=following_user)

        context.update({
            'follow_status':follow_status,
            'followings_count':followings_count,
            'followers_count':followers_count,
            'posts':posts,
        })
        return context