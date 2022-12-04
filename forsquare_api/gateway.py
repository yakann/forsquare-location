import requests as requests
from forsquare import settings


class FoursquareGateway(object):

    def _send_request(self, method, url, **kwargs):
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()
        return response

    def _get_headers(self, **kwargs):
        headers = {
            'Authorization': kwargs.get("token"),
            "Accept": "application/json",
        }
        return headers

    def _get_params(self, **kwargs):
        params = {"ll": "{},{}".format(str(kwargs.get("latitude")), str(kwargs.get("longitude")))}
        return params

    def get_place_data(self, latitude, longitude):
        url = "{}places/search".format(settings.FOURSQUARE_BASE_URL)
        token = {"token": settings.FOURSQUARE_TOKEN}
        import ipdb;ipdb.set_trace()
        params = self._get_params(**{"latitude": latitude, "longitude": longitude})

        import ipdb;
        ipdb.set_trace()
        headers = self._get_headers(**token)

        response = requests.request("GET", url, params=params, headers=headers)
        response.raise_for_status()

        return response.json()['results']