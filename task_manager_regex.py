import subprocess
import re


class TaskManager:
    def __init__(self):
        self.logs = []

    def execute_command(self, command):
        result = subprocess.run(
            command, capture_output=True, text=True, shell=True)
        self.logs.append(result.stdout)
        self.logs.append(result.stderr)
        return result.stdout

    def parse_logs(self):
        error_pattern = r"error|warning|cannot access|No such file or directory"
        errors = []
        for log in self.logs:
            errors.extend(re.findall(error_pattern, log, re.IGNORECASE))
        return errors


task_manager = TaskManager()
output = task_manager.execute_command("ls /nonexistent_directory")
# above I have passed a directory which doesn't exist so that I can get errors :)
errors = task_manager.parse_logs()
print(f"Errors found: {errors}")


# Notes


# subprocess.run()  :-
# subprocess.run() returns an object, which contains details about the executed command.
# Attributes of the object: result.stdout → Standard output (command output).
# result.stderr → Standard error (error messages, if any).
#  parameters of subprocess.run() ->
# capture_output=True -> Captures both stdout (standard output) and stderr (standard error),
# so they can be accessed programmatically.
# text=True -> Converts the output from bytes to a string, this is because subprocess.run()
# returns output as raw bytes
# shell=True -> Runs the command through the shell


# parse logs :-
# parse --> reading + extracting info from raw files
# Logs usually contain system messages, errors, warnings, and execution details, and parsing
# helps to filter and analyze them.
# Unlike self.logs, which stores command outputs permanently for later use, errors is only
# needed temporarily
# Each time parse_logs is called, it creates a fresh errors list, ensuring that previous errors
# don’t persist.
