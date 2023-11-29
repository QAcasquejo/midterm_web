from flask import Flask
from flask import request
from flask import render_template

sample = Flask(__name__)

@sample.route("/login")
def login():
    return render_template("login.html")

@sample.route("/registration")
def registration():
    return render_template("registration.html")


if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5000)
