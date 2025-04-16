import file1

print("This is file2.py")

# Conclusion
# To see the difference
# First run the file1.py then run file2.py
# What happens ?
# the block if __name__ == "__main__": in file1.py will not execute.
# The code inside it only runs when the file is run directly (i.e., not imported).


# When running file1.py directly, Python treats it as the main program,
# and __name__ is set to "__main__".
# When importing file1.py in file2.py, Python sets __name__ to "file1",
# so the code inside the if __name__ == "__main__": block is skipped.


# The if __name__ == "__main__": check allows you to control whether certain code
# should run when the file is run directly versus when it's imported into another script.
