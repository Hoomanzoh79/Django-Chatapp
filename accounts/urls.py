from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("edit-account/",views.EditAccountView.as_view(),name="edit-account"),
    path(r'?P<slug>[\w.@+-]+/',views.AccountDetailView.as_view(),name="account-detail"),
]