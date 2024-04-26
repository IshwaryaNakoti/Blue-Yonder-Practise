from flask import Blueprint

simple1_api = Blueprint('simple1_api', __name__)

@simple1_api.route('/simple1')
def action():
    return "simple1"
