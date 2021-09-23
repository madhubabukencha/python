"""
Using smtplib.smtp_ssl instead of smtplib.smtp we can avoid usage of
below code
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
Note : But we have to change port number to 465
"""

import os
import smtplib

email_user_name = os.environ.get('EMAIL_NAME')
email_password = os.environ.get('EMAIL_PASS')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_user_name, email_password)
    subject = "Sending mail using SMTP_SSL"
    body = "Great!!! you successfully send a mail"
    msg = f'Subject:{subject}\n\n{body}'
    smtp.sendmail(email_user_name, 'madhukencha.programmer@gmail.com', msg)
