from flask import Flask, render_template, request, redirect, url_for
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from getStudents import getStudents
from checkTime import checkTime
from getFreePeriod import getFreePeriod
from send import send


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


@app.route('/', methods=["GET", "POST"])
def home():
    # if the time is between 7:00 and 9:30 return active page, if time is outside 7:00 - 9:30 return the inactive page
    # store the students who login between 7:00 and 9:30 and send an email at 9:30 with the list
    if request.method == "GET":
        check = checkTime()
        if True:
            if daily.studentsGotten == True:
                return render_template("open.html", len=len(daily.students), students=daily.students)
            else:
                open()
                return render_template("open.html", len=len(daily.students), students=daily.students)

        elif check == False:
            return render_template("closed.html")

    # TODO(braid): Remove special closing check
        elif check == 3:
            if daily.emailSent == False:
                close()
            return render_template("closed.html")

    # There shouldn't be a post request that causes the form to open

    elif request.method == "POST":
        check = checkTime()
        if True:
            try:
                student = request.form.get("student")
                daily.students.remove(student)
            except:
                None

            return render_template("open.html", len=len(daily.students), students=daily.students)

        elif check == False:
            return render_template("closed.html")

    # TODO(braid): Remove special closing check
        elif check == 3:
            if daily.emailSent == False:
                close()
            return render_template("closed.html")


if __name__ == '__main__':
    app.run(debug=False, port=8000)
