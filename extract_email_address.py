import re


def extract_email_addresses(filename):
    with open(filename, 'r') as file:
        text = file.read()
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}'
        list_of_email = re.findall(email_pattern, text)
        return list_of_email


list_of_email = extract_email_addresses("random_phone_numbers.txt")


# lets make it more easier to read
for email in list_of_email:
    print(email)
