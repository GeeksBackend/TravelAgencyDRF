from rest_framework.generics import ListAPIView, CreateAPIView

from apps.tours.models import Tour
from apps.tours.serializers import TourSerializers

# Create your views here.
class TourAPI(ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializers

class TourAPICreate(CreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializers