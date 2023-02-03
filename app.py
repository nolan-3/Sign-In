from flask import Flask, render_template, request, redirect, url_for
import os
import threading
# on form submit use datetime to record the time (optional)
# once the time hits 9:30 shut down or something
import datetime
import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler


def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))


scheduler = BackgroundScheduler()
#scheduler.add_job(func=print_date_time, trigger="interval", seconds=1)
scheduler.add_job(func=print_date_time, trigger='cron', hour= 19, minute= '*')
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

app = Flask(__name__)

#COME UP WITH GOOD NAMES FOR THESE VARIABLES
#PERHAPS WRITE TO A TEXT FILE
class students:
    signedIn = []

daily = students()

# get data from free period list
data = ["TEST","TEST2", "TEST3","TEST4", "TEST5", "TEST6"]


def end():
    data = students.signedIn
    print(data)
#7200 seconds in 2 hours


@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        #check if time is after 9:30 not necessary?
        return render_template("index.html", len = len(data), data = data )
    elif request.method == "POST":
        #check if time is after 9:30
        checked = request.form.get("checked")
        daily.signedIn.append(checked)
        data.remove(checked)
        return render_template("index.html", len = len(data), data = data)
        
def timeFunction():
    #turn on at 7:30
    #send an email
    #close at 9:30
    #loop

    return render_template("useless.html")

if __name__ == '__main__':
        app.run(debug=True, port = 8000)