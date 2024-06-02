from django.views.generic import ListView
from django.contrib.auth import get_user_model

from accounts.models import CustomUser


class SearchResultsView(ListView):
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
