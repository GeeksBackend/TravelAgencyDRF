from django.urls import path 

from apps.tours.views import TourAPI, TourAPICreate


urlpatterns = [
    path('', TourAPI.as_view(), name="api_tours"),
    path('create/', TourAPICreate.as_view(), name="api_tours_create")
]