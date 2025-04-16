import os
import sys
from datetime import datetime
import shutil
import subprocess
import argparse


# Step 1: Set up the command-line argument parser

def parse_arguments():
    """
    This function sets up & parses command-line arguments
    It expects the user to provide a status message to log.
    """
    parser = argparse.ArgumentParser(
        description="Log system status with timestamps")
    parser.add_argument('status_message', type=str,
                        help="The system status message to log")

    return parser.parse_args()


# Step 2: Log the message with timestamp

def log_message(status_message):
    """
    This function takes the status message, adds a timestamp to it,
    & appends it to the log file
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {status_message}\n"
    log_file = "/home/avager/Desktop/parse_time_compress_main.log"
    with open(log_file, 'a') as file:
        file.write(log_entry)
    print(f"Log saved to {log_file}")


# Step 3: Create a backup of the log file

def backup_log():
    """
    This function creates a backup of the log file in a 'backups' directory
    & compress the backup into a tar.gz file
    """
    log_file = "/home/avager/Desktop/parse_time_compress_main.log"
    backup_dir = "backups"
    # create the backups dir if it doesn't exist
    # i.e. it will not raise any error if file exist
    os.makedirs(backup_dir, exist_ok=True)
    shutil.copy(log_file, backup_dir)
    print(f"Log file backed up to {backup_dir}/{log_file}")
    subprocess.run(
        ['tar', '-czf', f'{backup_dir}/backup_log.tar.gz', os.path.join(backup_dir, log_file)])
    print(f"Backup compressed to {backup_dir}/backup_log.tar.gz")


# Step 4: Main function to handle the flow of the program

def main():
    """
    The main entry point of the program
    It parses arguments
    Logs the message with timestamp
    Backs up the log file & compresses it 
    """
    args = parse_arguments()

    log_message(args.status_message)

    backup_log()


# if this script is run directly only then main function will be executed
# main motive is other functions will be executed only if the main function is executed.
if __name__ == "__main__":
    main()
