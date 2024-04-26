from flask import Blueprint

user2_api = Blueprint("user2_api", __name__)

@user2_api.route("/welcome/user2")
def greet():
    return "2"