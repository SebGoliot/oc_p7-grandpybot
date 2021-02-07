from flask import Flask, render_template, jsonify, request
from .parser import Parser
from .wiki_data import WikiData
from .maps_data import MapsData
from os import getenv

app = Flask(__name__)
maps_js_key = getenv('MAPS_JS_KEY')

@app.route("/")
def home():
    """Main route loading the index"""

    return render_template("home.html", maps_key=maps_js_key)


@app.route("/ask", methods=["POST"])
def ask():
    """AJAX route to query Grandpy"""

    msg = request.get_data().decode("utf-8")

    if not msg:
        return invalid_request()

    if user_request := Parser.parse_request(msg):

        if address := MapsData.get_address_from_request(user_request):
            page_id = WikiData.get_page_id_from_position(address[1])
            if desc := WikiData.get_page_desc_from_id(page_id):
                desc = f"Oh, et j'ai failli oublier :<br>{desc}"

            response = f"Bien sûr mon poussin ! Voici son adresse :<br> {address[0]}"
            
            return jsonify(
                {
                    "response": response,
                    "position": address[1],
                    "description": desc,
                    "page_id": page_id
                }
            )

    return invalid_request()


def invalid_request():
    return jsonify(
        {
            "response": "J'ai dû oublier...",
            "position": None,
            "description": None,
            "page_id": None
        }
    )
