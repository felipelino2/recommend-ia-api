from flask import Flask
from routes.routes_api import give_ia_response

app = Flask(__name__)
app.json.sort_keys = False
app.register_blueprint(give_ia_response)

app.run()
