from forsquare_api.exceptions import LocationDuplicatedFieldError, FoursquareLocationNotFoundException
from forsquare_api.gateway import FoursquareGateway
from forsquare_api.models import Location


class LocationService(object):
    gateway = FoursquareGateway()

    def _create_location_fields(self, latitude, longitude, places):
        for place in places:
            name = place.get("name")
            location_data = place.get("location")
            fsq_id = place.get("fsq_id")
            if location_data:
                address = location_data.get('formatted_address')
                region = location_data.get('region')
                country = location_data.get('country')
                location = Location(name=name, address=address, region=region, country=country, latitude=latitude,
                                    longitude=longitude, fsq_id=fsq_id)
                location.save()

    def create_location(self, **kwargs):
        latitude = kwargs.get('latitude')
        longitude = kwargs.get('longitude')
        try:
            Location.objects.get(latitude=latitude, longitude=longitude)
            raise LocationDuplicatedFieldError(latitude, longitude)
        except Location.MultipleObjectsReturned:
            raise LocationDuplicatedFieldError(latitude, longitude)
        except Location.DoesNotExist:
            pass
        places = self.gateway.get_place_data(latitude, longitude)
        if not places:
            raise FoursquareLocationNotFoundException
        self._create_location_fields(latitude, longitude, places)