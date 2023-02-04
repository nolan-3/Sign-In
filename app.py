from flask import Flask, render_template, request, redirect, url_for
import os
import threading
# on form submit use datetime to record the time (optional)
# once the time hits 9:30 shut down or something
import datetime
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from getStudents import getStudents


app = Flask(__name__)

#COME UP WITH GOOD NAMES FOR THESE VARIABLES
#PERHAPS WRITE TO A TEXT FILE
class students:
    signedIn = []

daily = students()

def open():
    #MAKE THIS DYNAMIC
    #MODULO IS INVOLVED, FIGURE OUT HOW
    #freePeriod = "B"
    
    #tudents = getStudents(freePeriod)
    #active(students)
    return testing()
    #turn on at 7:30
    #send an email
    #close at 9:30
    #loop
def close():
    students = students.signedIn
    print(students)
    return render_template("useless.html")
    

def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))


@app.route('/', methods = ["GET", "POST"])
def home():
        scheduler = BackgroundScheduler()
        scheduler.add_job(func=open, trigger="interval", seconds=1)
        #scheduler.add_job(func=print_date_time, trigger='cron', hour= 19, minute= '*')
        scheduler.start()

        # Shut down the scheduler when exiting the app
        #HMM DO I WANT THIS?
        atexit.register(lambda: scheduler.shutdown())
        return render_template("index.html", len = 0, students = ['inactive'] )
        
@app.route('/active', methods = ["GET","POST"])
def active(students=["test"]):
    if request.method == "GET":
        #check if time is after 9:30 not necessary?
        return render_template("index.html", len = len(students), students = students )
    elif request.method == "POST":
        #check if time is after 9:30
        checked = request.form.get("checked")
        daily.signedIn.append(checked)
        students.remove(checked)
        return render_template("index.html", len = len(students), students = students)

@app.route('/testing',)
def testing():
        with app.app_context:
            print("testing runs")
            render_template("test.html")
            return app

if __name__ == '__main__':
        app.run(debug=True, port = 8000)