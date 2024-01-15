class Listing():

    def __init__(self, id, name, description, cost, user_id):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.user_id = user_id

    def __eq__(self,other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Listing({self.id}, {self.name}, {self.description}, {self.cost}, {self.user_id})"