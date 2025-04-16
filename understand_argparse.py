import argparse

# Create a parser object
parser = argparse.ArgumentParser(description="A simple login script")

# Define expected arguments
# expecting argument username
parser.add_argument("username", help="Your username")
# expecting argument password
parser.add_argument("password", help="Your password")

# Parse the arguments
args = parser.parse_args()
print(args)

# Access the arguments
print(f"Username: {args.username}")
print(f"Password: {args.password}")
