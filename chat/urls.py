from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('',views.ChatIndexView.as_view(),name="chat-index"),
    path('<str:user1>/<str:user2>/',views.message,name="message"),
    # path("<str:room_name>/", views.room_view, name="room"),
]
