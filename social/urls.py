from django.urls import path

from . import views

app_name = 'social'

urlpatterns = [
    path('',views.SearchResultsView.as_view(),name="search"),
    path('follow/<str:username>/',views.FollowView.as_view(),name="follow"),
]
