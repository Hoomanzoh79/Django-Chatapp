from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("edit-account/",views.EditAccountView.as_view(),name="edit-account"),
    path("<int:pk>/",views.AccountDetailView.as_view(),name="account-detail"),
]