from rest_framework import serializers

from apps.tours.models import Tour


class TourSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tour 
        fields = "__all__"