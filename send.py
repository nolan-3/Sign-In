import smtplib
import ssl
from email.message import EmailMessage
import time
from getFreePeriod import getFreePeriod
from password import p
from getStudents import getStudents
# given a list of students, sends that list to a specified email address.

def send(students,unregisteredNames):
    dayOfWeek = time.strftime("%A")
    #if dayOfWeek == "Saturday" or dayOfWeek == "Sunday":
        #return
    #else:
    sendAll(students,unregisteredNames)
    sendGrades(students,unregisteredNames)
    sendStudents(students,unregisteredNames)


def sendAll(students,unregisteredNames):

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "haverfordsignin@gmail.com"  # Enter your address
    #################################### CHANGE TO KOLADE
    receiver_email = ["nolamccl@haverford.org","agreattofutaxpayer@gmail.com"]  # Enter receiver address
    password = p

    content = 'Name, Grade \n'
    for name in unregisteredNames:
        content += name + " " + students[name].grade + '\n'
    freePeriod = getFreePeriod()
    month = time.strftime("%B")
    day = str(int(time.strftime("%d")))
    dayOfWeek = time.strftime("%A")

    msg = EmailMessage()
    msg.set_content(content)
    tagLine = "Students Who Didn't Sign In " + dayOfWeek + " " + month + " " + day + " " + freePeriod + " Period"
    msg['Subject'] = tagLine
    msg['From'] = sender_email
    msg['To'] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg, from_addr=sender_email,
                            to_addrs=receiver_email)

def sendGrades(students,unregisteredNames):
    for i in range(0,4):
    ################################### CHANGE TO FORM DEANS
        if i == 0:
            target = "III"
            dean = "nolamccl@haverford.org"
        elif i == 1:
            target = "IV"
            dean = "nolamccl@haverford.org"
        elif i == 2:
            target = "V"
            dean = "nolamccl@haverford.org"
        elif i == 3:
            target = "VI"
            dean = "nolamccl@haverford.org"
        
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "haverfordsignin@gmail.com"  # Enter your address
        receiver_email = dean  # Enter receiver address
        password = p

        content = 'Missing Students from Form ' + target + '\n'

        for name in unregisteredNames:
            if(students[name].grade == target):
                content += name + '\n'

        freePeriod = getFreePeriod()
        month = time.strftime("%B")
        day = str(int(time.strftime("%d")))
        dayOfWeek = time.strftime("%A")

        msg = EmailMessage()
        msg.set_content(content)
        tagLine = "Students Who Didn't Sign In " + dayOfWeek + " " + month + " " + day + " " + freePeriod + " Period"
        msg['Subject'] = tagLine
        msg['From'] = sender_email
        msg['To'] = receiver_email

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.send_message(msg, from_addr=sender_email,
                                to_addrs=receiver_email)
        
        

def sendStudents(students,unregisteredNames):
    recipients = []
    recipients.append("haverfordsignin@gmail.com")
    #for name in unregisteredNames:
        #recipients.append(students[name].email)
    recipients.append("nolamccl@haverford.org")
    recipients.append("agreattofutaxpayer@gmail.com")

    print(f"sending emails to :{recipients}")

    #email = "agreattofutaxpayer@gmail.com"
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "haverfordsignin@gmail.com"  # Enter your address
    #receiver_email = email  # Enter receiver address
    password = p
    content = "you didn't sign in first period today"
    freePeriod = getFreePeriod()
    month = time.strftime("%B")
    day = str(int(time.strftime("%d")))
    dayOfWeek = time.strftime("%A")
    msg = EmailMessage()
    msg.set_content(content)
    tagLine = "You didn't sign in  " + dayOfWeek + " " + month + " " + day + " " + freePeriod + " Period"
    msg['Subject'] = tagLine
    msg['From'] = sender_email
    msg["Bcc"] = recipients

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg, from_addr=sender_email,
                            to_addrs=recipients,)