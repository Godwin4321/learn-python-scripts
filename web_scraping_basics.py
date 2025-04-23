from bs4 import BeautifulSoup
import requests

# Fetch data from this url
url = "https://bbc.com"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting all anchor tags from the page
for link in soup.find_all('a'):
    print(link.get('href'))


# soup.find_all('a')   <-- returns ResultSet which is iterable
# Eg:   <a href="/news">News</a>
# link.get('href')  <-- extracts the value of the href attribute
# from that <a> tag — which is usually the URL.
