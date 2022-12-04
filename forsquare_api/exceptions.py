class LocationDuplicatedFieldError(Exception):

    def __init__(self, latitude, longitude, message="Location already exist"):
        self.latitude = latitude
        self.longitude = longitude
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'latitude:{self.latitude}, longitude:{self.longitude} -> {self.message}'


class FoursquareLocationNotFoundException(Exception):

    def __init__(self, message="Remote location is not found"):
        self.message = message
        super().__init__(self.message)