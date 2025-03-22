class Server:
    def __init__(self, name, ip_address):
        self.name = name               # object with two attributes
        self.ip_address = ip_address

    def start(self):
        return f"{self.name} is starting."

    def stop(self):
        return f"{self.name} is stopping."


# Creating an object of the Server class
server1 = Server("WebServer1", "192.168.0.1")

# Accessing attribute of the object
print(server1.name)

# Accessing method of the object
print(server1.start())
