from flask import Flask
from datetime import datetime

app = Flask(__name__)

counter = 0


@app.route("/")
def welcome():
    return "Welcome to my Flash Cards application!"


@app.route("/date")
def date():
    return f"This page was served at {datetime.now()}"


@app.route("/counter")
def counter_view():
    global counter
    counter += 1
    return f"This page was viewed {counter} times."
