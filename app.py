from school_schedule import registration_open, free_period
from send import send
from password import server_password
from login import login_required
from getStudents import getStudents

from flask import Flask, render_template, request, redirect, session
from flask_session import Session


app = Flask(__name__, static_url_path='', static_folder='static',)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Manage the school schedule, and keep track of registered students
class RegistrationManager():

    # Constructor
    def __init__(self):

        # Always refresh on startup
        self.refreshStudents()

        # Setup recurring events to send mail, and refresh the student list
        if self.isOpen():
            self.awaiting = "close"
            #self.awaitClose()
        else:
            #self.awaitOpen()
            self.awaiting = "open"
        print("constructor runs!")
    # Destructor
    def __del__(self):
        # Shut down the recurring events when finished
        #self.cron.shutdown()
        None


    # Require a login to prevent outside users
    loggedIn = False
    #set initial user id number
    id = 0

    def checkLogin(self, guess):
        if guess == server_password:
            self.loggedIn = True
            return True
        else:
            return False
    # Properties
    # =========================
    # Check whether registration is currently open
    def isOpen(self):
        return registration_open()


    # Get the names of all currently unregistered students
    ## PROBLEM ##############################TODO#######################################################
    def unregisteredNames(self):
        return [name for name in self.students if self.students[name].signedIn == False]
    

    # If the program just switched from open -> close or vice versa perform open/closing tasks
    def checkChange(self):
        if self.awaiting == "open":
            if self.isOpen():
                self.refreshStudents()
                self.awaiting = "close"

        elif self.awaiting == "close":
            if not self.isOpen():
                self.sendMail()
                self.awaiting = "open"


    # Actions
    # =========================
    # Refresh the list of students for the current day
    def refreshStudents(self):
        print("Refreshing student list.")
        self.freePeriod = free_period()
        self.students = getStudents(self.freePeriod)

    # Send mail containing the list of unregistered students
    def sendMail(self):
        print("Sending mail.")
        send(self.students, self.unregisteredNames())

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

registration = RegistrationManager()


@app.route('/login', methods=["GET","POST"])
def login():
    session.clear()

    if request.method == "GET":
        return render_template("login.html")

    elif request.method == "POST":
        guess = request.form.get("guess")
        if registration.checkLogin(guess):
            session["user_id"] = registration.id
            registration.id += 1
            print("new user:")
            print(session["user_id"])
            return redirect("/")
        else:
            return render_template("login.html")




@app.route('/', methods=["GET", "POST"])
@login_required
def home():
    registration.checkChange()
    if not registration.loggedIn:
        return redirect("/login")

    # If this is a form submission, attempt to register the student
    if request.method == "POST":
        student = request.form["student"]
        print(f"Registering '{student}': {registration.register(student)}")
    # if the time is between 7:00 and 9:30 return active page, if time is outside 7:00 - 9:30 return the inactive page
    # store the students who login between 7:00 and 9:30 and send an email at 9:30 with the list
    if registration.isOpen():
        return render_template("open.html", names=registration.unregisteredNames())

    return render_template("closed.html")


if __name__ == '__main__':
    app.run(debug=False, port=8000)


