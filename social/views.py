from django.views import generic
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404,redirect
from django.urls import reverse
from django.contrib import messages

from accounts.models import CustomUser
from .models import Follow

class SearchResultsView(generic.ListView):
    model = CustomUser
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
        context.update({
            'search_query': self.request.GET.get("q"),
        })
        return context


class FollowView(generic.View):
    def get(self,request,username):
        follower = self.request.user
        followed = get_object_or_404(CustomUser,username=username)
        if Follow.objects.filter(follower=follower,followed=followed).exists():
             messages.warning(self.request,"You already followed this user !")
        else:
            Follow.objects.create(follower=follower,followed=followed)
            messages.success(self.request,"You successfully followed this user")
        return redirect("pages:home")
    
    def post(self,request):
        return HttpResponse("post")