from rest_framework import viewsets, mixins, generics

from forsquare_api.exceptions import FoursquareLocationNotFoundException, LocationDuplicatedFieldError
from forsquare_api.models import Location
from forsquare_api.serializer import LocationSerializer, LocationListSerializer
from forsquare_api.service import LocationService
from rest_framework import status
from rest_framework.response import Response


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    service = LocationService()

    def get_serializer_class(self):
        if self.action == 'list':
            return LocationListSerializer
        if self.action == 'create':
            return LocationSerializer

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        self.service.create_location(**validated_data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({"message": "Locations are created"}, status=status.HTTP_201_CREATED, headers=headers)
        except FoursquareLocationNotFoundException as e:
            return Response({"message": e.message}, status=status.HTTP_404_NOT_FOUND)
        except LocationDuplicatedFieldError as e:
            return Response({"message": e.message}, status=status.HTTP_200_OK)
