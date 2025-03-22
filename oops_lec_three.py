class VirtualMachine:
    def __init__(self, hostname, cpu, ram):
        self.hostname = hostname
        self.cpu = cpu
        self.ram = ram

    def start(self):
        return f"VM: {self.hostname} with {self.cpu} and {self.ram}GB RAM is starting."


class WebServerVM(VirtualMachine):
    def __init__(self, hostname, cpu, ram, domain):
        super().__init__(hostname, cpu, ram)
        self.domain = domain

    def host_website(self):
        return f"Hosting website {self.domain} on {self.hostname}"


web_server = WebServerVM("WebServer1", "4 vCPUs", 16, "example.com")

print(web_server.start())
print(web_server.host_website())
