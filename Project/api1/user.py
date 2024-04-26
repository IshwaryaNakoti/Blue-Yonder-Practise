from flask import Blueprint

user1_api = Blueprint("user1_api", __name__)

@user1_api.route('/welcome/user1')
def greet():
    return "1"
