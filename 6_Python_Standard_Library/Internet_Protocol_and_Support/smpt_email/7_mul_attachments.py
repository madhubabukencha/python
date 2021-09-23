"""
In this program we will see how to send multiple attachments.
"""
import smtplib
import imghdr
import os
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get("EMAIL_NAME")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

msg = EmailMessage()
msg['Subject'] = "Attaching multiple images"
msg.set_content("In this mail attaching multiple images")
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'madhukencha.programmer@gmail.com'

images_list = ['albert_einstein.jpg', 'nature.jpg']
for image in images_list:
    with open(image, "rb") as f:
        image_data = f.read()
        image_type = str(imghdr.what(f.name))
        image_name = f.name
    msg.add_attachment(image_data, maintype="image", subtype=image_type, filename=image_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
