from django.urls import path

from apps.users.views import UserAPI

urlpatterns = [
    path('', UserAPI.as_view(), name="api_users")
]