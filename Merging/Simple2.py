from flask import Blueprint

simple2_api = Blueprint("simple2_api", __name__)

@simple2_api.route('/simple2')
def simple2():
    return "simple2"


