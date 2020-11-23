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
                            "formatted_address": "10 Quai de la Charente, 75019 Paris, France"
                        }
                    ],
                    "status": "OK",
                }

        test_address = "10 Quai de la Charente, 75019 Paris, France"

        def mock_request(*args, **kwargs):
            return mock_data()

        monkeypatch.setattr(requests, "get", mock_request)

        assert self.maps.get_address("openclassrooms") == test_address
