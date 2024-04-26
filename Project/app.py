from flask import Flask
from api1.user import user1_api
from api2.user import user2_api


app = Flask(__name__)
app.register_blueprint(user1_api)
app.register_blueprint(user2_api)

@app.route('/welcome')
def welcome():
    return "Welcome to the Esko website"


if __name__ == '__main__':
    app.run(debug=True)
