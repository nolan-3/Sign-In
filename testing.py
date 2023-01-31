import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "nolamccl@haverford.org"  # Enter your address
receiver_email = "nolamccl@haverford.org"  # Enter receiver address
password = 'input("Type your password and press enter: ")'
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


# import smtplib, ssl
# from email.message import EmailMessage

# port = 465  # For SSL
# smtp_server = "smtp.gmail.com"
# sender_email = "sender@gmail.com"  # Enter your address
# receiver_email = "receiver@gmail.com"  # Enter receiver address
# password = "16-digit-app-password"

# msg = EmailMessage()
# msg.set_content("Hello Underworld!")
# msg['Subject'] = "Hello Underworld from Python Gmail!"
# msg['From'] = sender_email
# msg['To'] = receiver_email

# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)