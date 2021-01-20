from flaskr.parser import Parser


class TestParser:
    def setup(self):
        self.parser = Parser()

        self.parsing_requests_test = [
            ("Où se trouve Marseille ?", "marseille"),
            ("Tu pourrais me dire où se situe Cannes ?", "cannes"),
            ("Papy ! Parle moi de Toulon !", "toulon"),
            ("Qu'est-ce que tu peux me dire sur Lyon ?", "lyon"),
            ("Tu pourrais me parler d'Arles ?", "arles"),
            ("Où est Montpellier ??", "montpellier"),
            ("Raconte moi l'histoire d'Avignon.", "avignon"),
            ("Qu'est-ce que tu peux me dire à propos de Nice?", "nice"),
            ("Adresse de la Poste à Arles", "la poste a arles"),
            ("Salut Grandpy", None)
        ]

    def test_parse_request(self):
        """Check that the parser returns meaningful information"""
        
        for request, result in self.parsing_requests_test:
            assert self.parser.parse_request(request) == result
