from django.urls import path 

from apps.tours.views import TourAPI, TourAPICreate, TourAPIRetrieve, TourAPIUpdate, TourAPIDestroy


urlpatterns = [
    path('', TourAPI.as_view(), name="api_tours"),
    path('create/', TourAPICreate.as_view(), name="api_tours_create"),
    path('<int:pk>/', TourAPIRetrieve.as_view(), name="api_tours_retrieve"),
    path('update/<int:pk>/', TourAPIUpdate.as_view(), name="api_tours_update"),
    path('destroy/<int:pk>/', TourAPIDestroy.as_view(), name="api_tours_destroy")
]