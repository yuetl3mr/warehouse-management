from flask import Blueprint, render_template, request

# Define a blueprint
home_bp = Blueprint("products", __name__)

@home_bp.route("/products", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return "Login via POST method!"
    else:
        return render_template("login.html")
