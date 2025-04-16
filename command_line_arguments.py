import sys

if len(sys.argv) != 3:
    print("Usage: python3 command_line_arguments.py <username> <password>")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]

print(f"Hello {username} ! Your password is {password}")
