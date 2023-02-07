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
    daily.freePeriod = getFreePeriod()
    daily.students = getStudents(daily.freePeriod)
    daily.emailSent = False

def close(): 
    notSignedIn = daily.students
    send(notSignedIn)
    daily.emailSent = True


@app.route('/', methods = ["GET","POST"])
def home():
    check = checkTime()
    if request.method == "GET":
        if check == True:
            return render_template("open.html", len = len(daily.students), students = daily.students)
        elif check == False:
            return render_template("closed.html")
        elif check == 2:
            open()
            return render_template("open.html", len = len(daily.students), students = daily.students)
        elif check == 3:
            if daily.emailSent == False:
                close()
            close()
            return render_template("closed.html")


    elif request.method == "POST":
        check = checkTime()
        if check == True:
            student = request.form.get("checked")
            daily.students.remove(student)
            return render_template("open.html", len = len(daily.students), students = daily.students)
        elif check == False:
            return render_template("closed.html")
        elif check == 2:
            open()
            return render_template("open.html", len = len(daily.students), students = daily.students)
        elif check == 3:
            if daily.emailSent == False:
                close()
            return render_template("closed.html")


if __name__ == '__main__':
        app.run(debug=False, port = 8000)