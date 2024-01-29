from rest_framework import serializers

from apps.news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News 
        fields = ('id', 'user', 'title',
                  'description', 'image')