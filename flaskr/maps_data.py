from typing import Dict, Tuple, Union
import requests
from os import getenv


class MapsData:

    maps_key = getenv('MAPS_KEY')

    maps_api_uri = (
        "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    )

    @staticmethod
    def get_address_from_request(
        request: str
    ) -> Union[Tuple[str, Dict[str, str]], None]:

        request_args = {
            "input": request,
            "inputtype": "textquery",
            "fields": "formatted_address,geometry",
            "key": MapsData.maps_key,
        }

        data = requests.get(url=MapsData.maps_api_uri, params=request_args)

        try:
            data = data.json().get("candidates")[0]
            formatted_address = data.get("formatted_address")
            location = data.get("geometry").get("location")
        except:
            return None

        if formatted_address and location:
                return (formatted_address, location)

        return None
