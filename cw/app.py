from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/name")
def hello_class():
    return "<p>Hello, class!</p>"
