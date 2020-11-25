import requests
from flaskr.maps_data import MapsData


class TestMapsData:
    def setup(self):
        self.maps = MapsData()

    def test_get_address(self, monkeypatch):
        """Check if get_address returns the expected address"""

        class mock_data:
            def json(self):
                return {
                    "candidates": [
                        {
                            "formatted_address": "10 Quai de la Charente, 75019 Paris, France",
                            "geometry": {
                                "location": {
                                    "lat": 48.8975156,
                                    "lng": 2.3833993,
                                },
                                "viewport": {
                                    "northeast": {
                                        "lat": 48.89886702989273,
                                        "lng": 2.384756379892722,
                                    },
                                    "southwest": {
                                        "lat": 48.89616737010729,
                                        "lng": 2.382056720107278,
                                    },
                                },
                            },
                        }
                    ],
                    "status": "OK",
                }

        test_address = (
            "10 Quai de la Charente, 75019 Paris, France",
            {"lat": 48.8975156, "lng": 2.3833993},
        )

        def mock_request(*args, **kwargs):
            return mock_data()

        monkeypatch.setattr(requests, "get", mock_request)

        assert (
            self.maps.get_address_from_request("openclassrooms") == test_address
        )
