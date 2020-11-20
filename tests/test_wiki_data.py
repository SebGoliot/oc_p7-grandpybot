import requests
from flaskr.wiki_data import WikiData


class TestWikiData:

    test_data = {
        "query": {
            "pages": {
                "5036603": {
                    "extract": "Le musée des Civilisations de l'Europe et de la Méditerranée (Mucem) est un musée national situé à Marseille. Il a été inauguré par le président François Hollande, le 7 juin 2013, alors que Marseille était Capitale européenne de la culture. Il constitue l'un des rares témoignages pérennes de la programmation culturelle de l'année 2013 conçue par B. Latarjet, avec la construction du FRAC PACA dans le nouveau quartier de la Joliette.\nMusée de société,, le Mucem est un musée national placé sous la tutelle du Ministère de la Culture et consacré aux civilisations de l’Europe et de la Méditerranée. Sa création à Marseille souligne le souci de l'Etat de doter la deuxième ville de France d'un équipement culturel majeur. \nLes expositions permanentes sont globalement conçues en croisant différents champs scientifiques : anthropologie, archéologie, histoire,  histoire de l’art et art contemporain. Le musée propose également des expositions temporaires monographiques consacrés à des artistes ou personnalités majeures du monde de la création plastique et littéraire. Le musée a vocation à rendre compte des permanences historiques et sociales de ce bassin de civilisation, ainsi que des tensions qui le traversent jusqu’à l’époque contemporaine.\nComme pour tous les musées selon la définition de l'ICOM, et les principes de la loi musées en France, le Mucem associe à sa programmation d'expositions, une riche programmation culturelle: comme un forum, il se veut un lieu de débats, et la programmation artistique et culturelle, ainsi que les expositions, s'attachent à aborder de grandes questions qui animent les sociétés européennes et méditerranéennes contemporaines. \nLe Mucem est présidé par Jean-François Chougnet depuis 2015; il a succédé à Bruno Suzzarelli qui a organisé le chantier de préfiguration à partir de 2009, dans le cadre des grands travaux soutenus par Patrick Devedjian. Le directeur scientifique du Mucem depuis 2011 est Zeev Gourarier, conservateur général du patrimoine. \nDepuis son inauguration, le Mucem a accueilli 8,5 millions de visiteurs, dont 2,2 millions dans ses espaces d'exposition entre 2013 et 2016. Le musée est donc présenté comme un outil d'attractivité du territoire de la métropole d'Aix Marseille. En 2015, le Mucem a reçu le prix du Musée du Conseil de l'Europe.",
                }
            },
        },
    }

    wiki_desc_test = "Le musée des Civilisations de l'Europe et de la Méditerranée (Mucem) est un musée national situé à Marseille. Il a été inauguré par le président François Hollande, le 7 juin 2013, alors que Marseille était Capitale européenne de la culture. Il constitue l'un des rares témoignages pérennes de la programmation culturelle de l'année 2013 conçue par B. Latarjet, avec la construction du FRAC PACA dans le nouveau quartier de la Joliette."

    def setup(self):
        self.wiki_data = WikiData()

    def test_get_desc(self):

        assert self.wiki_data.get_desc(self.test_data) == self.wiki_desc_test

    def test_query_wiki(self, monkeypatch):
        """Check that the query_wiki returns the correct data """

        class mock_data:
            def json(self):
                return TestWikiData.test_data

        def mock_request(*args, **kwargs):
            return mock_data()

        monkeypatch.setattr(requests, "get", mock_request)

        assert self.wiki_data.query_wiki("mucem") == self.test_data

    def test_get_page_desc_from_search(self):
        """Check that the get_page_desc_from_search returns the correct
        description from a search
        """

        assert (
            self.wiki_data.get_page_desc_from_search("mucem")
            == self.wiki_desc_test
        )

    def test_get_page_id_from_position(self):
        """Check that the get_page_id_from_position returns the correct page id
        from a position
        """

        test_position = {"lat": 43.2966667, "lng": 5.3599999}
        assert (
            self.wiki_data.get_page_id_from_position(test_position) == 5036603
        )

    def test_get_page_desc_from_id(self):
        """Check that the get_page_desc_from_id returns the correct description
        from a page id
        """

        assert (
            self.wiki_data.get_page_desc_from_id(5036603) == self.wiki_desc_test
        )
