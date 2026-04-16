class Vault:
    def __init__(self, data=None):
        self.data = data or {}

    def add(self, name, username, password):
        self.data[name] = {
            "username": username,
            "password": password
        }

    def get(self, name):
        return self.data.get(name)

    def list(self):
        return list(self.data.keys())