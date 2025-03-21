import os


def check_file_size(file_path):
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)  # get file size in bytes
        return file_size
    else:
        print("File does not exist")
        return None


# Let's ask the user to enter the path of the file
file_path = input("Enter the file path: ")

# Let's print the file size
file_size = check_file_size(file_path)
if file_size is not None:
    print(
        f"File size of {file_path} is {file_size/1024}KB and {file_size/(1024*1024)}MB")
else:
    print("Unable to calculate file size because the file was not found.")
