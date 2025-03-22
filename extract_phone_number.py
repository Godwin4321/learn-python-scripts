import re


def extract_phone_numbers(filename):
    with open(filename, 'r') as file:
        text = file.read()
        phone_pattern = r'\d{3}-\d{3}-\d{4}'
        phone_numbers = re.findall(phone_pattern, text)
        return phone_numbers


phone_numbers = extract_phone_numbers("random_phone_numbers.txt")
print(phone_numbers)


# If the file does not exist in the current folder then give the full
# path of the file
