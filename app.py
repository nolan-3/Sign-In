from flask import Flask, render_template, request
from apscheduler.schedulers.background import BackgroundScheduler
from getStudents import getStudents
from checkTime import checkTime
from getFreePeriod import getFreePeriod
from send import send
import atexit


app = Flask(__name__, static_url_path='', static_folder='static',)


# store the data of each day in an object
class info:
    freePeriod = getFreePeriod()
    students = getStudents(freePeriod)
    # it isn't actually necessary to have both
    emailSent = False
    studentsGotten = True


daily = info()


# Shut down the scheduler when exiting the app
# HMM DO I WANT THIS?
atexit.register(lambda: scheduler.shutdown())


def open():
    daily.freePeriod = getFreePeriod()
    daily.students = getStudents(daily.freePeriod)
    daily.emailSent = False
    daily.studentsGotten = True


def close():
    send(daily.students)
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


# schedule the close function to run at 9:30
scheduler = BackgroundScheduler()
scheduler.add_job(func=close, trigger='cron', hour=9, minute=30)
scheduler.start()


@app.route('/', methods=["GET", "POST"])
def home():
    # If this is a form submission, attempt to register the student
    if request.method == "POST":
        register(request.form["student"])

    # if the time is between 7:00 and 9:30 return active page, if time is outside 7:00 - 9:30 return the inactive page
    # store the students who login between 7:00 and 9:30 and send an email at 9:30 with the list
    check = checkTime()
    if check == True:
        if daily.studentsGotten == True:
            names = [
                name for name in daily.students if daily.students[name].signedIn == False]
            return render_template("open.html", names=names)
        # only runs if the program is running for multiple days straight, open is called initially at the start of the program
        else:
            open()
            return render_template("open.html", names=names)

    elif check == False:
        return render_template("closed.html")


if __name__ == '__main__':
    app.run(debug=False, port=8000)
