import requests
from grandpy.wiki_data import WikiData


class TestWikiData:

    test_data = {
        "query": {
            "pages": {
                "5036603": {
                    "pageid": 5036603,
                    "title": "Musée des Civilisations de l'Europe et de la Méditerranée",
                    "extract": "Le Musée des Civilisations de l'Europe et de la Méditerranée (Mucem) est un musée national situé à Marseille. Il a été inauguré par le président François Hollande, le 7 juin 2013, alors que Marseille était Capitale européenne de la culture. Il constitue l'un des rares témoignages pérennes de la programmation culturelle de l'année 2013 conçue par Bernard Latarjet, avec la construction du FRAC PACA dans le nouveau quartier de la Joliette.\nMusée de société,, le Mucem est un musée national placé sous la tutelle du Ministère de la Culture et consacré aux civilisations de l’Europe et de la Méditerranée.",
                }
            }
        }
    }

    test_geosearch = {
        "query": {
            "geosearch": [
                {
                    "pageid": 5036603,
                    "title": "Musée des Civilisations de l'Europe et de la Méditerranée",
                    "lat": 43.2967,
                    "lon": 5.36,
                }
            ]
        },
    }

    wiki_desc_test = "Le Musée des Civilisations de l'Europe et de la Méditerranée (Mucem) est un musée national situé à Marseille. Il a été inauguré par le président François Hollande, le 7 juin 2013, alors que Marseille était Capitale européenne de la culture. Il constitue l'un des rares témoignages pérennes de la programmation culturelle de l'année 2013 conçue par Bernard Latarjet, avec la construction du FRAC PACA dans le nouveau quartier de la Joliette."

    def setup(self):
        self.wiki_data = WikiData()

    def test_extract_desc(self):

        assert (
            self.wiki_data.extract_desc(self.test_data) == self.wiki_desc_test
        )


    def test_query_wiki(self, monkeypatch):
        """Check that the query_wiki returns the correct data """

        class mock_data:
            def json(self):
                return TestWikiData.test_data

        def mock_request(*args, **kwargs):
            return mock_data()

        monkeypatch.setattr(requests, "get", mock_request)

        assert self.wiki_data.query_wiki("mucem") == self.test_data


    def test_get_page_desc(self, monkeypatch):
        """Check if we can get a correct description from a search or an id"""

        class mock_data:
            def json(self):
                return TestWikiData.test_data

        def mock_request(*args, **kwargs):
            return mock_data()

        monkeypatch.setattr(requests, "get", mock_request)

        assert (
            self.wiki_data.get_page_desc_from_search("mucem")
            == self.wiki_desc_test
        )

        assert (
            self.wiki_data.get_page_desc_from_id(5036603) == self.wiki_desc_test
        )


    def test_get_page_id_from_position(self, monkeypatch):
        """Check that the get_page_id_from_position returns the correct page id
        from a position
        """

        class mock_data:
            def json(self):
                return TestWikiData.test_geosearch

        def mock_request(*args, **kwargs):
            return mock_data()

        monkeypatch.setattr(requests, "get", mock_request)

        test_position = {"lat": 43.2966667, "lng": 5.3599999}
        assert (
            self.wiki_data.get_page_id_from_position(test_position) == 5036603
        )
