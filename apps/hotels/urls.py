from django.urls import path 

from apps.hotels.views import HotelAPI

urlpatterns = [
    path('', HotelAPI.as_view(), name='api_hotels')
]