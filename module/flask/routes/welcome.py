from flask import Blueprint

hello_flask = Blueprint('apiflask', __name__)


@hello_flask.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
