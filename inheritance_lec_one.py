class Server:
    def __init__(self, name, ip_address):
        self.name = name               # object with two attributes
        self.ip_address = ip_address

    def start(self):
        return f"{self.name} is starting."

    def stop(self):
        return f"{self.name} is stopping."


class DatabaseServer(Server):  # DatabaseServer class inherits from Server class
    def __init__(self, name, ip_address, database_name):
        super().__init__(name, ip_address)  # calling constructor of parent class
        self.database_name = database_name

    def start(self):
        return f"Database server {self.name} with database {self.database_name} is starting"


# Creating a DatabaseServer object
db_server = DatabaseServer("DBServer1", "192.198.0.2", "MySQL")

# Calling method
print(db_server.start())
