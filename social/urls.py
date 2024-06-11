from django.urls import path

from . import views

app_name = 'social'

urlpatterns = [
    path('',views.SearchResultsView.as_view(),name="search"),
    path('follow/<str:username>/<option>',views.follow,name="follow"),
    path('<str:username>/followers',views.FollowersList.as_view(),name="followers-list"),
    path('<str:username>/followings',views.FollowingsList.as_view(),name="followings-list"),
    path('post/<int:pk>',views.PostDetailView.as_view(),name="post-detail"),
    path('post/create',views.PostCreateView.as_view(),name='post-create'),
    path('post/like/<int:pk>/<option>',views.like,name="like"),
]
