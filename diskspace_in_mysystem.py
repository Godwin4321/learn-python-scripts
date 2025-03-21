import os  # importing os module to interact with the os


def check_disk_space(path):  # funct to check disk space
    statvfs = os.statvfs(path)
    free_space = statvfs.f_frsize * statvfs.f_bavail
    return free_space


# Let's check the disk space for root directory
path = "/"
free_space = check_disk_space(path)

# Print the available space in MB
print(f"Free space in {path} is {free_space / (1024*1024)} MB")


# Note:
# os.statvfs() -> returns filesystem statistics about a given path
# free_space = statvfs.f_frsize * statvfs.f_bavail
# statvfs.f_frsize → Fragment size (block size in bytes)
# statvfs.f_bavail → Number of free blocks available to normal users
# free_space → Total free space in bytes (only for normal users)

# 1 byte = 8 bits, each bit can be either 0 or 1
# 1024 Bytes = 1 Kilobyte (KB)
# 1024 Kilobytes (KB) = 1 Megabyte (MB)
# 1024 Megabyte (MB) = 1 Gigabyte (GB)

# 1 MB = 1024 KB × 1024 Bytes = 1,048,576 Bytes
# So, the division is necessary to convert bytes into MB

# To convert bytes to KB divide by 1024
# To convert bytes to MB divide by 1024 * 1024
