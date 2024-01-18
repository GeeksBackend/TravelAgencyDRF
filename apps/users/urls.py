from django.urls import path

from apps.users.views import UserAPI, UserRegisterAPI

urlpatterns = [
    path('', UserAPI.as_view(), name="api_users"),
    path('register/', UserRegisterAPI.as_view(), name="api_users_register")
]
