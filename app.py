from flask import Flask, render_template, request, redirect, url_for
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from getStudents import getStudents
from checkTime import checkTime
from getFreePeriod import getFreePeriod
from send import send


app = Flask(__name__)

#PERHAPS WRITE TO A TEXT FILE
class info:
    freePeriod = getFreePeriod()
    students = getStudents(freePeriod)
    emailSent = False

daily = info()

def open():
    with app.app_context:
        return url_for('/active')

def close():
    notSignedIn = info.students
    send(notSignedIn)
    return render_template("useless.html")
    

@app.route('/', methods = ["GET","POST"])
def home():
    if request.method == "GET":
        #if checkTime() == True:
        if True:
            return render_template("open.html", len = len(info.students), students = info.students)
        else:
            return render_template("closed.html")

    elif request.method == "POST":
        #check if time is after 9:30
        student = request.form.get("checked")
        info.students.remove(student)
        #if checkTime() == True:
        if True:
            return render_template("open.html", len = len(info.students), students = info.students )
        else:
            return render_template("closed.html")


if __name__ == '__main__':
        app.run(debug=True, port = 8000)