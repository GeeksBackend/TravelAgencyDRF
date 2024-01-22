from rest_framework.generics import ListAPIView

from apps.hotels.models import Hotel
from apps.hotels.serializers import HotelSerializer

# Create your views here.
class HotelAPI(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer