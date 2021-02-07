from grandpy.stop_words import stop_words
import re
import unidecode


class Parser:

    _REGEX_PARSE = [
        r"parle moi (de|du|d) (.*)",
        r"parler (de|du|d) (.*)",
        r"(dire|sait|quelque chose) sur (.*)",
        r"se (trouve|situe) (.*)",
        r"ou est ()(.*)",
        r"histoire (de|du|d) (.*)",
        r"a propos (de|du|d) (.*)",
        r"adresse (de|du|d) (.*)",
    ]

    @classmethod
    def parse_request(cls, request):
        """Returns the body of the request """

        request = cls._clean_request(request)
        regex_out = cls._run_regex(cls._REGEX_PARSE, request)

        if regex_out:
            return regex_out

        # If the parser doesn't get anything from the regex
        # return the request without stopwords
        return cls._remove_stopwords(request)

    @staticmethod
    def _run_regex(regex, request):
        """Runs a list of regex against a request
        returns the first successfull regex search
        """

        for reg in regex:
            regex_parse = re.search(reg, request)
            if regex_parse:
                return regex_parse.group(2)
        return None

    @staticmethod
    def _clean_request(request):
        """Removes punctuation and diacritics from the request """

        request = re.sub(r"\W", " ", request.lower())
        request = [word for word in request.split(" ") if word != ""]
        request = str(unidecode.unidecode(" ".join(request)))
        return request

    @staticmethod
    def _remove_stopwords(request):
        """Removes stopwords from the request """

        request = [word for word in request.split(" ") if word != ""]
        request = [word for word in request if word not in stop_words]
        if request:
            return " ".join(request)

        return None