from datetime import datetime

current_time = datetime.now()

formatted_time = current_time.strftime("%d-%m-%Y %H:%M")

status_message = f"System check: {formatted_time}"

log_file = "/home/avager/Desktop/Learn Python/datetime_activity.log"
with open(log_file, "a") as file:
    file.write(status_message + "\n")
# opening the file with append access
# \n will append my message into new line

print(f"Log saved to {log_file}")
