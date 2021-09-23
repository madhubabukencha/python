"""
In this program we will see how to set Subject, Body, From and To
address instead of using format string method
"""
import smtplib
from email.message import EmailMessage
import os

# Taking credential from environment
EMAIL_ADDRESS = os.environ.get('EMAIL_NAME')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# Adding Subject, Body, From and To address
msg = EmailMessage()
msg['Subject'] = "Using mail.message Package"
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'madhukencha.programmer@gmail.com'
msg.set_content("This mail send using email.message and smtplib packages")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
