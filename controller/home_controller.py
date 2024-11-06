from flask import Blueprint

# Define a blueprint
home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    return "Hello, World!"