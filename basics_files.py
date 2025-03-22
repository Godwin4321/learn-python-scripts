filename = "random_phone_numbers.txt"

with open(filename, 'r') as file:  # 'file' is a variable that holds the opened file object
    text = file.read()

print(text)

# The with statement ensures that the file is automatically closed after reading,
# preventing resource leaks.
# file.read() returns the entire content of the file as a string.
# file is an object of the file class. You can use any name instead of file
