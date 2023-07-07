from flask import Flask

app = Flask(__name__)

app.debug = True

@app.route("/")
def welcome():
    return "Hello, world"


from controller import user_controller, product_controller
