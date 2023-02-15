import smtplib
import ssl
from email.message import EmailMessage
import time
from getFreePeriod import getFreePeriod
# given a list of students, sends that list to a specified email address.


def send(students):
    print(students)
    if students == None:
        return
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "haverfordsignin@gmail.com"  # Enter your address
    receiver_email = "nolamccl@haverford.org"  # Enter receiver address
    password = "xndbajmzcwgalbwo"

    content = ''
    for i in range(0, len(students)):
        content += students[i] + '\n'
    freePeriod = getFreePeriod()
    month = time.strftime("%B")
    month = time.strptime(month, '%B').tm_mon
    day = str(int(time.strftime("%d")))

    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = "Sign In Attendance " + \
        day + " " + " " + freePeriod + " period"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg, from_addr=sender_email,
                            to_addrs=receiver_email)
