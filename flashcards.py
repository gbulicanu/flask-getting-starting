from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to my Flash Cards application!"


@app.route("/date")
def date():
    return f"This page was served at {datetime.now()}"
