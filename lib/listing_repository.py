from lib.listing import Listing

class ListingRepository():
    
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM listings')
        listings = []
        for row in rows:
            listing = Listing(row["id"], row["name"], row["description"], row["cost"], row["user_id"])
            listings.append(listing)
        return listings
    
    def find_by_user(self, user_id):
        rows = self._connection.execute('SELECT * FROM listings WHERE user_id = %s', [user_id])
        listings = []
        for row in rows:
            listing = Listing(row["id"], row["name"], row["description"], row["cost"], row["user_id"])
            listings.append(listing)
        return listings
    
    def create(self, name, description, cost, user_id):
        self._connection.execute('INSERT INTO listings (name, description, cost, user_id) VALUES (%s, %s, %s, %s)', 
                                [name, description, cost, user_id])
        return None
    
    def delete(self, id):
        self._connection.execute('DELETE FROM listings WHERE id = %s', [id])
        return None