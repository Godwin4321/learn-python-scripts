import datetime

# current_time = datetime.datetime.now()
# print(current_time)

# formatted_time = current_time.strftime("%d-%m-%Y %H:%M")
# print(formatted_time)

# Date in string format
user_input_date = "07/04/2025 11:11"

# 07/04/2025
#  |  |   |
# %d %m  %Y

# Convert string data into object format
date_object = datetime.datetime.strptime(user_input_date, "%d/%m/%Y %H:%M")

print(date_object)
