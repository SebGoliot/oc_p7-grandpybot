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
            "fields": "formatted_address",
            "key": maps_key,
        }

        data = requests.get(url=MapsData.maps_place_api_uri, params=request_args)

        if data := data.json():
            if address := data["candidates"][0]:
                if formatted_address := address["formatted_address"]:
                    return formatted_address

        return None
