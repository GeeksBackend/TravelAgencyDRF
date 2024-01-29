from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.news.models import News
from apps.news.serializers import NewsSerializer

# Create your views here.
class NewsAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = News.objects.all()
    serializer_class = NewsSerializer