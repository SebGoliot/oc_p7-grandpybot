from flaskr import app
from os import environ

# The following 'keys' import are for debug purposes only !
# The keys file should NOT be included with the source code
# or copied to the production server.
# Also, the production wsgi server should NOT run this file,
# but the flaskr package instead and get his API keys from
# environment variables.
# See README.md for more information.
from keys import maps_key, maps_js_key

if __name__ == "__main__":
    environ['MAPS_KEY'] = maps_key
    environ['MAPS_JS_KEY'] = maps_js_key

    app.run(host="0.0.0.0", port=5050, debug=True)
