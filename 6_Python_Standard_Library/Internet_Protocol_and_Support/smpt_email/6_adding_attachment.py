"""
In this program we will see how to add an attachment to the mail
"""
import smtplib
import imghdr
import os
from email.message import EmailMessage

MAIL_ADDRESS = os.environ.get('EMAIL_NAME')
MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = "Adding an attachment"
msg.set_content("Adding an attachment")
msg['From'] = MAIL_ADDRESS
msg['TO'] = 'madhukencha.programmer@gmail.com'

with open('albert_einstein.jpg', "rb") as f:
    file_data = f.read()
    file_name = f.name
    file_type = str(imghdr.what(f.name))
    print("Type :", file_type)
msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(MAIL_ADDRESS, MAIL_PASSWORD)
    smtp.send_message(msg)



