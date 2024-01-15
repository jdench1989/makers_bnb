from lib.listing_repository import ListingRepository
from lib.listing import Listing
from lib.database_connection import DatabaseConnection

# all() method returns a list of all Listings for given user_id

def test_all_returns_all_listings(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = ListingRepository(db_connection)
    result = repository.all()
    assert result == [
                    Listing(1, 'Cosy Woodland Lodge', 'Embrace the quirky, cosy interiors in this romantic getaway. Open the doors to the terrace, and let the sounds of nature waft through the lodge.', 45, 1),
                    Listing(2, 'Barn with a Vineyard View', 'Nestled in open countryside next to our vineyard on the outskirts of Bishops Stortford, an ideal base to explore East Herts & North Essex or visit London & Cambridge.', 70, 1),
                    Listing(3, 'Luxurious treehouse', 'Clad in aromatic cedar wood, beautifully furnished - ideal  private, woodland retreat for couples. Can also comfortably sleep up to 2 children (from 5 years) on single mattresses in loft area accessed by a ladder and hatch.', 35, 2),
                    Listing(4, '2BD Luxury Apartment', 'Come and stay in our beautifully designed luxury apartment, right in the heart of Kidbrooke Village! Super chic and private, with incredible views of London this luxury apartment is a home from home.', 50, 3),
                    Listing(5, 'Immaculate City Penthouse', 'A bright one bed apartment with huge 43m2 south facing terrace with stunning views of Canary Wharf. Located on Commercial Rd this 5th floor residence offers guests the perfect place to stay in East London. ', 100, 2),
                    Listing(6, 'Snowdrop Pod Glamping', 'Snowdrop Pod is set in its own garden with stunning views overlooking the Colne Valley.  The pod offers en suite shower & toilet, kitchette with fridge and cooker and BBQ/Firepit.', 85, 1)]

# find_by_user() lists all listings associated with given user_id
def test_find_by_user_returns_given_users_listings(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = ListingRepository(db_connection)
    result = repository.find_by_user(3)
    assert result == [Listing(4, '2BD Luxury Apartment', 'Come and stay in our beautifully designed luxury apartment, right in the heart of Kidbrooke Village! Super chic and private, with incredible views of London this luxury apartment is a home from home.', 50, 3)]

# create() adds a new listed to the database 
def test_create_adds_new_listing(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = ListingRepository(db_connection)
    repository.create('Beautiful seaside caravan', 'A delightful static caravan located just a ten minute walk from Southend seafront. It has two bedrooms and sleeps a total of 8 people', 38, 3)
    result = repository.all()
    assert result == [
                    Listing(1, 'Cosy Woodland Lodge', 'Embrace the quirky, cosy interiors in this romantic getaway. Open the doors to the terrace, and let the sounds of nature waft through the lodge.', 45, 1),
                    Listing(2, 'Barn with a Vineyard View', 'Nestled in open countryside next to our vineyard on the outskirts of Bishops Stortford, an ideal base to explore East Herts & North Essex or visit London & Cambridge.', 70, 1),
                    Listing(3, 'Luxurious treehouse', 'Clad in aromatic cedar wood, beautifully furnished - ideal  private, woodland retreat for couples. Can also comfortably sleep up to 2 children (from 5 years) on single mattresses in loft area accessed by a ladder and hatch.', 35, 2),
                    Listing(4, '2BD Luxury Apartment', 'Come and stay in our beautifully designed luxury apartment, right in the heart of Kidbrooke Village! Super chic and private, with incredible views of London this luxury apartment is a home from home.', 50, 3),
                    Listing(5, 'Immaculate City Penthouse', 'A bright one bed apartment with huge 43m2 south facing terrace with stunning views of Canary Wharf. Located on Commercial Rd this 5th floor residence offers guests the perfect place to stay in East London. ', 100, 2),
                    Listing(6, 'Snowdrop Pod Glamping', 'Snowdrop Pod is set in its own garden with stunning views overlooking the Colne Valley.  The pod offers en suite shower & toilet, kitchette with fridge and cooker and BBQ/Firepit.', 85, 1),
                    Listing(7, 'Beautiful seaside caravan', 'A delightful static caravan located just a ten minute walk from Southend seafront. It has two bedrooms and sleeps a total of 8 people', 38, 3)]
    
# delete() removes a listed space from the database
def tests_delete_removes_listing_from_db(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = ListingRepository(db_connection)
    repository.delete(6)
    result = repository.all()
    assert result == [
                    Listing(1, 'Cosy Woodland Lodge', 'Embrace the quirky, cosy interiors in this romantic getaway. Open the doors to the terrace, and let the sounds of nature waft through the lodge.', 45, 1),
                    Listing(2, 'Barn with a Vineyard View', 'Nestled in open countryside next to our vineyard on the outskirts of Bishops Stortford, an ideal base to explore East Herts & North Essex or visit London & Cambridge.', 70, 1),
                    Listing(3, 'Luxurious treehouse', 'Clad in aromatic cedar wood, beautifully furnished - ideal  private, woodland retreat for couples. Can also comfortably sleep up to 2 children (from 5 years) on single mattresses in loft area accessed by a ladder and hatch.', 35, 2),
                    Listing(4, '2BD Luxury Apartment', 'Come and stay in our beautifully designed luxury apartment, right in the heart of Kidbrooke Village! Super chic and private, with incredible views of London this luxury apartment is a home from home.', 50, 3),
                    Listing(5, 'Immaculate City Penthouse', 'A bright one bed apartment with huge 43m2 south facing terrace with stunning views of Canary Wharf. Located on Commercial Rd this 5th floor residence offers guests the perfect place to stay in East London. ', 100, 2)]