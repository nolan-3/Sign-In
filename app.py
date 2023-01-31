from flask import Flask, render_template, request, redirect, url_for
import os
# on form submit use datetime to record the time (optional)
# once the time hits 9:30 shut down or something
import datetime

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html", data = "TESTING" )
    elif request.method == "POST":
        print("We haven't gotten this far yet")


if __name__ == '__main__':
        app.run(debug=True, port = 8000)