from flask import Flask, render_template, request
from apscheduler.schedulers.background import BackgroundScheduler
from getStudents import getStudents
from pytz import timezone
from getFreePeriod import getFreePeriod
from send import send
#from datetime import datetime, time
import datetime
import time

# All times are localized and interpreted in this timezone.
TIMEZONE = timezone("America/New_York")

OPEN_TIME = datetime.time(7, 0)
CLOSE_TIME = datetime.time(9, 45)



# Manage the school schedule, and keep track of registered students
class RegistrationManager():
    # All times are localized and interpreted in this timezone.

    # Constructor
    def __init__(self):
        # Setup recurring events to send mail, and refresh the student list
        self.cron = BackgroundScheduler()
        self.cron.add_job(func=lambda: self.sendMail(),
                          trigger='cron',
                          hour=CLOSE_TIME.hour,
                          minute=CLOSE_TIME.minute,
                          timezone=TIMEZONE)
        self.cron.add_job(func=lambda: self.refreshStudents(),
                          trigger='cron',
                          hour=OPEN_TIME.hour,
                          minute=OPEN_TIME.minute,
                          timezone=TIMEZONE)
        self.cron.start()

        # Always refresh on startup
        self.refreshStudents()

    # Destructor
    def __del__(self):
        # Shut down the recurring events when finished
        self.cron.shutdown()

    # Properties
    # =========================
    # Check whether registration is currently open
    def isOpen(self):
        timeNow = datetime.datetime.now(TIMEZONE).strftime("%A")
        if isWednesday():
            return (OPEN_TIME <= timeNow) and (timeNow <= datetime.time(10, 15))
        else:
            return (OPEN_TIME <= timeNow) and (timeNow <= CLOSE_TIME)
    

    # Get the names of all currently unregistered students
    def unregisteredStudents(self):
        return [name for name in self.students if self.students[name].signedIn == False]

    # Actions
    # =========================
    # Refresh the list of students for the current day
    def refreshStudents(self):
        print("Refreshing student list.")
        self.freePeriod = getFreePeriod()
        self.students = getStudents(self.freePeriod)

    # Send mail containing the list of unregistered students
    def sendMail(self):
        print("Sending mail.")
        send(self.unregisteredStudents())

    # Attempt to register a student name, returns false if there's an error
    def register(self, student):
        if not self.isOpen():
            return "Error: Registration is not open"

        if student not in self.students:
            return "Error: Student not found"

        if self.students[student].signedIn:
            return "Warning: Student already signed in"

        self.students[student].signedIn = True
        return "Ok"
    
    def isWednesday(self):
        dayOfWeek = datetime.datetime.now(TIMEZONE).strftime("%A")
        return(dayOfWeek == "Wednesday")


registration = RegistrationManager()

app = Flask(__name__, static_url_path='', static_folder='static',)

@app.route('/', methods=["GET", "POST"])
def home():
    # If this is a form submission, attempt to register the student
    if request.method == "POST":
        student = request.form["student"]
        print(f"Registering '{student}': {registration.register(student)}")
    # if the time is between 7:00 and 9:30 return active page, if time is outside 7:00 - 9:30 return the inactive page
    # store the students who login between 7:00 and 9:30 and send an email at 9:30 with the list
    if registration.isOpen():
        return render_template("open.html", names=registration.unregisteredStudents())

    return render_template("closed.html")


if __name__ == '__main__':
    app.run(debug=False, port=8000)
