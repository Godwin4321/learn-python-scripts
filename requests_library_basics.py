import requests

url = 'https://bbc.com'
response = requests.get(url)

if response.status_code == 200:
    print("Successful")
else:
    print("Failed")

print(response.text)

# response.text converts the HTML (or other content) of the website into a string.
# This means that whatever content is returned by the server in the response,
# response.text gives you that content as a string.
# For example, when you fetch a webpage (like the BBC homepage),
# response.text contains the HTML markup of that page, converted into string.
