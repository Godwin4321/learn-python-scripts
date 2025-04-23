import os
import requests
import csv
from bs4 import BeautifulSoup

# Path of my csv file
custom_path = "/home/avager/Desktop/articles.csv"

# Ensure the folder exists (if not, create it)
os.makedirs(os.path.dirname(custom_path), exist_ok=True)

# Fetch data from the url
url = 'https://cnn.com'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Open the csv file at the custom path to write the data
with open(custom_path, 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the CSV Header
    writer.writerow(['Title', 'Link'])

    # Find all <a> tags with a href attribute
    articles = soup.find_all('a', href=True)

    # Loop through each article and extract the title and link
    for article in articles:
        title = article.get_text(strip=True)
        link = article['href']  # get the value of href

        if link.startswith('/'):
            link = "https://cnn.com" + link

        # if both title and link exist only then it will be added to the CSV file
        if title and link:
            writer.writerow([title, link])


# File saved to :
print(f"Data saved to {custom_path}")
