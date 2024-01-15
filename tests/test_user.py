from lib.user import User

# Instantiates with the email and password stored correctly
def test_user_instantiates_correctly():
    user = User(1, "test-email", "test-password", "Test user name 1")
    assert user.id == 1
    assert user.email == "test-email"
    assert user.password == "test-password"

def test_identical_instances_equal_for_testing():
    user1 = User(1, "test-email", "test-password", "Test user name 1")
    user2 = User(1, "test-email", "test-password", "Test user name 1")
    assert user1 == user2

def test_string_formatting():
    user = User(1, "test-email", "test-password", "Test user name 1")
    assert str(user) == "User(1, test-email, test-password, Test user name 1)"
