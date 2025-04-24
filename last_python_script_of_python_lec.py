import requests
import pandas as pd
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import shutil
import re
from datetime import datetime

# Function to scrape website and save data


def scrape_website():
    url = 'https://bbc.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = []
    for article in soup.find_all('a', {'class': 'promo-link'}):
        title = article.get_text()
        link = article.get('href')
        data.append([title, link])

    # Save data to CSV
    df = pd.DataFrame(data, columns=['Title', 'Link'])
    df.to_csv('scraped_data.csv', index=False)


def backup_logs():
    logs_dir = '/path/to/logs'
    # backup_2025.03.08_12:31:45
    backup_dir = f'/path/to/backups/backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    shutil.make_archive(backup_dir, 'zip', logs_dir)

# Function to parse logs


def parse_logs():
    with open('system.log', 'r') as file:
        logs = file.readlines()
    error_logs = [log for log in logs if re.search(r'ERROR', log)]
    return error_logs

# Function to send an email notification


def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'admin@example.com'
    with smtplib.SMTP('smtp.example.com') as server:
        server.login('your_email@example.com', 'password')
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

# Main DevOps pipeline function


def devops_pipeline():
    # Step 1: Scrape the website
    scrape_website()

    # Step 2: Back up logs
    backup_logs()

    # Step 3: Parse logs for errors
    error_logs = parse_logs()

    # Step 4: Send email alert if errors found
    if error_logs:
        send_email('Critical Error Alert', '\n'.join(error_logs))


# Run the full pipeline
devops_pipeline()


# Notes
# data.append([title, link]) line is executed for each article, your data list will look like a list of lists
# Eg:
# data = [
#      ['Article 1', 'https://bbc.com/article1'],
#      ['Article 2', 'https://bbc.com/article2']
# ]

# pd.DataFrame() is a function in the Pandas library that is used to create a DataFrame, which is a 2D,
# tabular data structure (similar to a table in a database)
# It takes input data (such as a list, dictionary, or another DataFrame) and converts it into a DataFrame.
# The index=False argument in the df.to_csv() function tells Pandas not to write the row indices
# (default 0, 1, 2, ...) to the CSV file.

# {'class': 'promo-link'}: This is a filter for selecting only those <a> tags that have a class attribute
# equal to 'promo-link'.

# In pandas, to save a DataFrame to a CSV file, you should use the to_csv() method


# shutil.make_archive(backup_dir, 'zip', logs_dir)

# shutil.make_archive() is a function used to create archive files (like .zip or .tar).
# backup_dir is the name and path of the archive file you want to create (without the .zip extension).
# 'zip' tells it to create a ZIP file.
# logs_dir is the folder you want to compress.
