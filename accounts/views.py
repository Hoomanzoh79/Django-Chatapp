from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")


class EditAccountView(LoginRequiredMixin,generic.UpdateView):
    form_class = CustomUserChangeForm
    template_name = "accounts/edit_account.html"
    success_url = reverse_lazy("pages:home")


    def get_object(self):
        username = self.request.user.username
        account = get_object_or_404(CustomUser,username=username)
        return account