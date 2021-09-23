"""
SMTP          : Simple Mail Transfer Protocol
Documentation :https://docs.python.org/3/library/smtplib.html
"""
import smtplib
import os

# Environment variable
EMAIL_ADDRESS = os.environ.get('EMAIL_NAME')
# I sent two step authentication, that's why
# I'm not using password
EMAIL_HOST_PASS = os.environ.get('Django_App')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    # To yourself with ESMTP server using  EHLO
    smtp.ehlo()
    # To encrypt our traffic
    smtp.starttls()
    # To re-identify as a encrypted connection
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_HOST_PASS)
    subject = "About python email programming !!!"
    body = "It is a powerful programming language for mailing"
    msg = f'Subject:{subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
