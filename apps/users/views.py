from rest_framework.generics import ListAPIView, CreateAPIView

from apps.users.models import User
from apps.users.serializers import UserSerializer, UserRegisterSerializer

# Create your views here.
class UserAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegisterAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer