from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template, current_app
import atexit

app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def home():
        # scheduler = BackgroundScheduler()
        # scheduler.add_job(func=open, trigger="interval", seconds=1)
        # #scheduler.add_job(func=print_date_time, trigger='cron', hour= 19, minute= '*')
        # scheduler.start()

        # # Shut down the scheduler when exiting the app
        # #HMM DO I WANT THIS?
        # atexit.register(lambda: scheduler.shutdown())
        return render_template("index.html", len = 0, students = ['inactive'] )

scheduler = BackgroundScheduler()
#@scheduler.task('interval', id='render_template', seconds=1)
def render_template_task(app):
    print("render_template_task runs!")
    with app.app_context():
    #with current_app.app_context():
        return render_template("test.html")

def run_scheduler(app):
    #scheduler = BackgroundScheduler()
    scheduler.add_job(render_template_task, trigger="interval", seconds=1, args=[app])
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    run_scheduler(app)
    app.run()