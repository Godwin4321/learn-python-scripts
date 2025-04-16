config_data = """
 [general]
 username = admin
 password = oldpassword123
 [settings]
 deploy_directory = /var/www/app
 server_ip = 192.168.1.1
"""

# Removing extra newlines or spaces at the beginning and end of config_data (with .strip()).
lines = config_data.strip().split("\n")
print(lines)  # here lines is a list.
# lines = ['[general]', ' username = admin', ' password = oldpassword123',
#          ' [settings]', ' deploy_directory = /var/www/app', ' server_ip = 192.168.1.1']
print("\n")

for line in lines:
    print(f"'{line.strip()}'")

print("\n")


# split each line into key-value pairs
for line in lines:
    stripped_line = line.strip()
    if '=' in stripped_line:
        # unpacking a list of two elements into
        # two variables (key and value)
        key, value = stripped_line.split('=', 1)
        print(f"Key: {key.strip()}, Value: {value.strip()}")

print("\n")


# replace old password with a new one
updated_config = config_data.replace("oldpassword123", "newpassword456")


cleaned_lines = []
for line in lines:
    cleaned_line = line.strip()
    if '=' in cleaned_line:
        key, value = cleaned_line.split("=", 1)
        cleaned_lines.append(f"{key.strip()} = {value.strip()}")
    else:
        cleaned_lines.append(cleaned_line)

final_config = "\n".join(cleaned_lines)
print(final_config)
