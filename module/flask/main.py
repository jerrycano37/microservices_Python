from flask import Flask
from flask_cors import CORS
from module.flask.routes.welcome import hello_flask
from waitress import serve

app = Flask(__name__)


def create_app():
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.register_blueprint(hello_flask, url_prefix='/api')
    return app


def start_flask():
    app_ok = create_app()
    app_ok.run(host='127.0.0.1', port=3000)
    # serve(app_ok)
