# List of servers
servers = ["server1", "server2", "server3", "server4"]

# Status of servers
server_status = {
    "server1": "online",
    "server2": "offline",
    "server3": "terminated",
    "server4": "crashed"
}

for server in servers:
    status = server_status.get(server, "Unknown")
    if status == "terminated":
        print(f"{server} is terminated.")
    elif status == "crashed":
        print(f"{server} is crashed.")
    elif status == "offline":
        print(f"{server} is offline.")
    elif status == "online":
        print(f"{server} is online.")
    else:
        print(f"{status} status")


# Note:
# In python, we use get() method primarily with dictionaries
# We use get() method to get an item by its key
# here, server_status.get(server, "Unknown")
#     It means if the key exists it will return its value
#     If the key doesn't exist it will return "Unknown"
