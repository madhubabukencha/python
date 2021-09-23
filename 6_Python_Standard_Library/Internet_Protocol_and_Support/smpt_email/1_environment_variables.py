import os

email = os.environ.get('EMAIL_NAME')
password = os.environ.get('Django_App')

print(email)
print(password)