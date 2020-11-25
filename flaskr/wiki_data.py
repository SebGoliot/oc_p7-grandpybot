import requests


class WikiData:
    @classmethod
    def get_page_desc_from_search(cls, request):

        search_args = {
            "action": "query",
            "uselang": "fr",
            "format": "json",
            "prop": "extracts",
            "titles": request,
            "exintro": 1,
            "explaintext": 1,
            "redirects": 1,
        }
        data = cls.query_wiki(search_args)
        return cls.extract_desc(data)

    @classmethod
    def get_page_id_from_position(cls, position):

        search_args = {
            "action": "query",
            "uselang": "fr",
            "format": "json",
            "list": "geosearch",
            "gscoord": f"{position['lat']}|{position['lng']}",
            "gsradius": "100",
            "gslimit": "1",
        }
        data = cls.query_wiki(search_args)

        try:
            return data["query"]["geosearch"][0]["pageid"]
        except:
            return None

    @classmethod
    def get_page_desc_from_id(cls, page_id):

        search_args = {
            "action": "query",
            "uselang": "fr",
            "format": "json",
            "prop": "extracts",
            "pageids": page_id,
            "explaintext": 1,
            "redirects": 1,
        }
        data = cls.query_wiki(search_args)
        return cls.extract_desc(data)

    @classmethod
    def get_page_desc_from_position(cls, position):
        page_id = cls.get_page_id_from_position(position)
        desc = cls.get_page_desc_from_id(page_id)
        return desc

    @staticmethod
    def extract_desc(data):

        try:
            data = data["query"]["pages"]
            extract = data[str(*data)]["extract"]
        except KeyError:
            return None

        return extract.split("\n")[0]

    @staticmethod
    def query_wiki(search_args):

        wiki_api_uri = "https://fr.wikipedia.org/w/api.php"
        data = requests.get(url=wiki_api_uri, params=search_args)

        return data.json()
