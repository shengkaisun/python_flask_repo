class User():
    def __init__(self, id, name, password):
        self.username = name
        self.id = id
        self.password = password
    
    def __str__(self):
        return f"User ID: {self.id}"