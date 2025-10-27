from flask import Flask
from routes.routes_api import give_ia_response
from flask_cors import CORS

app = Flask(__name__)
app.json.sort_keys = False
app.register_blueprint(give_ia_response)

CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

