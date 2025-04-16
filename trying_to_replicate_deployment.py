import time

user_input = input(
    "Are you sure you want to deploy the application? (yes/no)").lower()

if user_input != "yes":
    print("Deployment cancelled")
    exit(0)  # will terminate the program successfully

env = input(
    "Which environment you would like to deploy to? (production/staging)").lower()

if env == "production":
    print("Deploying to production...")
    # waits for 2 seconds before continuing to the next line of code.
    time.sleep(2)
elif env == "staging":
    print("Deploying to staging...")
    time.sleep(2)
else:
    print("Invalid environment. Deployment failed.")


# time.sleep(2) -> Will wait for 2 seconds, then proceed.
# Makes the deployment feel a bit more "realistic." 😄
