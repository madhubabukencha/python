# To test locally we have to this code.


# TODO: Run below command:
# C:\Users\madhubabu>python -m smtpd -c DebuggingServer -n localhost:1025

import smtplib
import os

# Environment variable
EMAIL_ADDRESS = os.environ.get('EMAIL_NAME')

with smtplib.SMTP('localhost', 1025) as smtp:
    subject = "About python email programming !!!"
    body = "It is a powerful programming language for mailing"
    msg = f'Subject:{subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
