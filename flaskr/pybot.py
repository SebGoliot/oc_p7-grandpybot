from flask import Flask, render_template, jsonify, request
from .parser import Parser
from .wiki_data import WikiData
from .maps_data import MapsData

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/ask", methods=["POST"])
def ask():

    msg = request.get_data().decode("utf-8")
    desc, address = None, None

    if not msg:
        return invalid_request()

    if user_request := Parser.parse_request(msg):

        if address := MapsData.get_address_from_request(user_request):
            page_id = WikiData.get_page_id_from_position(address[1])
            desc = WikiData.get_page_desc_from_id(page_id)

            response = f"Bien sûr mon poussin ! Voici son adresse :\n {address[0]}"
            return jsonify(
                {
                    "response": response,
                    "position": address[1],
                    "description": desc
                }
            )

    return invalid_request()


def invalid_request():
    return jsonify({"response": "J'ai dû oublier..."})
