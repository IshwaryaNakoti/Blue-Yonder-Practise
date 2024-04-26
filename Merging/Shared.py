from flask import Flask
from Simple1 import simple1_api
from Simple2 import simple2_api

app = Flask(__name__)
app.register_blueprint(simple1_api)
app.register_blueprint(simple2_api)

@app.route('/')
def home():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
