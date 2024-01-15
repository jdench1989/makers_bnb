class User():

    def __init__(self, id, email, password, user_name):
        self.id = id
        self.email = email
        self.password = password
        self.user_name = user_name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User({self.id}, {self.email}, {self.password}, {self.user_name})"