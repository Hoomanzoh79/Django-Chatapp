from django.views import generic
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model

from accounts.models import CustomUser
from .models import Follow

class SearchResultsView(generic.ListView):
    model = get_user_model()
    template_name = "social/search_results.html"
    context_object_name = 'users'

    def get_queryset(self):  # new
        search_query = self.request.GET.get("q")
        if not search_query:
            search_query = ""
        object_list = self.model.objects.filter(
            username__icontains=search_query
        )
        return object_list

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        search_query = self.request.GET.get("q")
        following = self.model.objects.filter(
            username__icontains=search_query
        )
        for user in following.all():
            follower = self.request.user
            # Follow status
            follow_status = Follow.objects.filter(following=user,follower=follower).exists()

        context.update({
            'search_query': self.request.GET.get("q"),
            'follow_status':follow_status,
        })
        return context

def follow(request,username,option):
    user = request.user
    following = get_object_or_404(get_user_model(),username=username)
    try:
        f, created = Follow.objects.get_or_create(follower=user,following=following)

        if int(option) == 0 :
            f.delete()
        return HttpResponseRedirect(reverse("accounts:account-detail",kwargs={"slug":username}))
    except CustomUser.DoesNotExist:
        return HttpResponseRedirect(reverse("accounts:account-detail",kwargs={"slug":username}))