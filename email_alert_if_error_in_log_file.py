import smtplib
from email.mime.text import MIMEText
import re  # regular expression module

# Function to send an email notification


def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'admin@example.com'

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('your_email@example.com', 'password')
        server.sendmail(msg['From'], [msg['To']], msg.as_string())


# Read logs and parse for errors
with open('system.log', 'r') as file:
    logs = file.readlines()

# Find critical errors
critical_errors = [log for log in logs if re.search(r'ERROR', log)]

if critical_errors:
    send_email('Critical Error Alert', '\n'.join(critical_errors))
    print("Email sent for critical errors.")


# Notes

# with open('system.log', 'r') as file:
# This opens the file in read mode ('r'). If system.log does not exist, Python will raise a FileNotFoundError.
# If you want to create the file if it doesn't exist, you should open it in write ('w') or append ('a') mode instead.

# logs = file.readlines()
# logs = file.readlines() reads all the lines from the file and stores them as a list of strings,
# where each string is a line from the file.
#  if system.log contains:
# INFO: System started
# ERROR: Failed to load module
# WARNING: Low memory
# Then logs will be:
# [
#   "INFO: System started\n",
#   "ERROR: Failed to load module\n",
#   "WARNING: Low memory\n"
# ]


# critical_errors list will look like this:
# [
#     "ERROR Disk read failure\n",
#     "ERROR Network timeout\n"
# ]

# The .join() function takes any iterable — not just lists.
# All elements of the iterable must be strings, otherwise .join() will raise a TypeError.
# Once you apply .join() to a list, it returns a single string, not a list anymore.


# '\n'.join(critical_errors)

# The '\n'.join(critical_errors) takes all the strings in the critical_errors list and joins them into
# one single string, with each item separated by a new line (\n).

# The part before .join() is the separator that will be placed between each item of the list
# when they're joined together.
