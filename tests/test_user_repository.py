from lib.database_connection import DatabaseConnection
from lib.user_repository import UserRepository
from lib.user import User
import hashlib

# Calling all() method lists all users
def test_all_method_lists_all_users(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = UserRepository(db_connection)
    users = repository.all()
    assert users == [
        User(1, 'testemail1@example.com', 'c2852cf707649f8392a055b4598e84206f13628b6f5807b1c8a6711b2598ef42', 'Charles Boyle'),
        User(2, 'testemail2@example.com', '6eee3a5257a1329afe1dceb4ce1ebe0018e63a0788313253d3ec023228521ff2', 'Amy Santiago'),
        User(3, 'testemail3@example.com', '187154941ec7f71e45f09cc85f5dc956329cee757bd1f8e1b1b2f34a4d7e0600', 'Gina Linetti')
    ]

# create() adds new user to database
def test_create_method_adds_new_user(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = UserRepository(db_connection)
    repository.create('testemail4@example.com', 'test-password-4', 'Raymond Holt')
    users = repository.all()
    assert users == [
        User(1, 'testemail1@example.com', 'c2852cf707649f8392a055b4598e84206f13628b6f5807b1c8a6711b2598ef42', 'Charles Boyle'),
        User(2, 'testemail2@example.com', '6eee3a5257a1329afe1dceb4ce1ebe0018e63a0788313253d3ec023228521ff2', 'Amy Santiago'),
        User(3, 'testemail3@example.com', '187154941ec7f71e45f09cc85f5dc956329cee757bd1f8e1b1b2f34a4d7e0600', 'Gina Linetti'),
        User(4, 'testemail4@example.com', '14b609f073d95e8c1472d314fb23215328608cc26f44a1ad0ba069978aea2a44', 'Raymond Holt')
    ]

# check_password() compares hashed password attempt vs stored hash for given email
# return true for password match
def test_check_password_method_returns_true(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = UserRepository(db_connection)
    result = repository.check_password('testemail1@example.com', 'test-password-1')
    assert result == True

# check_password() compares hashed password attempt vs stored hash for given email
# return false for password mismatch
def test_check_password_method_returns_false(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = UserRepository(db_connection)
    result = repository.check_password('testemail1@example.com', 'wrong_password')
    assert result == False

# find_by_email() returns correct user
def test_find_by_email(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = UserRepository(db_connection)
    user = repository.find_by_email('testemail1@example.com')
    assert user == User(1, 'testemail1@example.com', 'c2852cf707649f8392a055b4598e84206f13628b6f5807b1c8a6711b2598ef42', 'Charles Boyle')


