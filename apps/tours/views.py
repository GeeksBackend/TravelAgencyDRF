from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from apps.tours.models import Tour
from apps.tours.serializers import TourSerializers

# Create your views here.
class TourAPI(ListAPIView):
    queryset = Tour.objects.all() #SELECT * FROM tours_tour; (Django ORM)
    serializer_class = TourSerializers

class TourAPICreate(CreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializers

class TourAPIRetrieve(RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializers

class TourAPIUpdate(UpdateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializers

class TourAPIDestroy(DestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializers