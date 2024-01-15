from lib.listing import Listing

# Listing class instantiates correctly
def test_class_instantiates_correctly():
    listing = Listing(1, 'first listing', 'listing description', 35, 1)
    assert listing.id == 1
    assert listing.name == 'first listing'
    assert listing.description == 'listing description'
    assert listing.cost == 35
    assert listing.user_id == 1

# Instances with identical values are considered equal for testing
def test_instances_equality_with_identical_values():
    listing1 = Listing(1, 'first listing', 'listing description', 35, 1)
    listing2 = Listing(1, 'first listing', 'listing description', 35, 1)
    assert listing1 == listing2

# Instance returns nicely formatted string when printed
def test_string_formatting():
    listing = Listing(1, 'first listing', 'listing description', 35, 1)
    assert str(listing) == "Listing(1, first listing, listing description, 35, 1)"