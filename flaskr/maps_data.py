import requests
from .secrets import maps_key


class MapsData:

    maps_place_api_uri = (
        "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    )

    @staticmethod
    def get_address(request):

        request_args = {
            "input": request,
            "inputtype": "textquery",
            "fields": "formatted_address,geometry",
            "key": maps_key,
        }

        data = requests.get(
            url=MapsData.maps_place_api_uri, params=request_args
        )

        data = data.json().get("candidates")[0]
        formatted_address = data.get("formatted_address")
        location = data.get("geometry").get("location")

        if formatted_address and location:
            return (formatted_address, location)

        return None
