from flask import Flask, render_template, request, redirect, url_for
from apscheduler.schedulers.background import BackgroundScheduler
from getStudents import getStudents
from checkTime import checkTime
from getFreePeriod import getFreePeriod
from send import send
from threading import Timer


app = Flask(__name__, static_url_path='', static_folder='static',)

# PERHAPS WRITE TO A TEXT FILE

# store the data of each day in an object


class info:
    freePeriod = getFreePeriod()
    students = getStudents(freePeriod)
    # it isn't actually necessary to have both
    emailSent = False
    studentsGotten = True


daily = info()


def open():
    daily.freePeriod = getFreePeriod()
    daily.students = getStudents(daily.freePeriod)
    daily.emailSent = False
    daily.studentsGotten = True


def close():
    notSignedIn = daily.students
    send(notSignedIn)
    daily.emailSent = True
    daily.studentsGotten = False

# Attempt to register a student
def register(student):
    if checkTime() != True:
        return False

    try:
        daily.students[student].signedIn = True
        return True
    except:
        return False


@app.route('/', methods=["GET", "POST"])
def home():
    # If this is a form submission, attempt to register the student
    if request.method == "POST":
        register(request.form["student"])

    # Render a response page
    # if the time is between 7:00 and 9:30 return active page, if time is outside 7:00 - 9:30 return the inactive page
    # store the students who login between 7:00 and 9:30 and send an email at 9:30 with the list
    check = checkTime()
    if check == True:
        if daily.studentsGotten == True:
            names = [name for name in daily.students if daily.students[name].signedIn == False]
            return render_template("open.html", names=names)
        else:
            open()
            
            return render_template("open.html", names=names)

    elif check == False:
        return render_template("closed.html")

    elif check == 3:
        if daily.emailSent == False:
            close()
        return render_template("closed.html")


if __name__ == '__main__':
    app.run(debug=False, port=8000)
