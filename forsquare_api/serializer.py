from rest_framework import serializers

from forsquare_api.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('latitude', 'longitude')


class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"