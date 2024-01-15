import os
from flask import Flask, request, render_template, session, redirect
from lib.user_repository import UserRepository
from lib.database_connection import get_flask_database_connection
from dotenv import load_dotenv
from lib.listing_repository import ListingRepository
from jinja2 import Environment, FileSystemLoader

load_dotenv()

# Create a new Flask app
app = Flask(__name__)
app.secret_key = os.environ["APP_SECRET_KEY"]

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/', methods=['GET'])
def get_index():
    if 'user_id' not in session:
        return render_template('index.html')
    else:
        return redirect('/account_page')

@app.route('/', methods=['POST'])
def create_user():
    email = request.form['email']
    password = request.form['password']
    user_name = request.form['user_name']
    password_confirmation = request.form['password_confirmation']
    password_match = None
    if password == password_confirmation:
        password_match = True
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        repository.create(email, password, user_name)
        return redirect("/login")
    else:
        password_match = False
        return render_template('index.html', password_match=password_match)

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def post_login():
    email = request.form['email']
    password_attempt = request.form['password']
    valid_password = None
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    if repository.check_password(email, password_attempt):
        user = repository.find_by_email(email)
        session['user_id'] = user.id
        session['user_name'] = user.user_name
        return redirect('/account_page')
    else:
        valid_password = False
        return render_template('login.html', valid_password = valid_password)
    
@app.route('/signout')
def get_signout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect('/')

@app.route('/account_page')
def account_page():
    if 'user_id' not in session:
        return redirect('/login')
    else:
        connection = get_flask_database_connection(app)
        repository = ListingRepository(connection)
        listings = repository.find_by_user(session['user_id'])
        user_name = session['user_name']
        return render_template('account_page.html', listings = listings, user_name = user_name)
    
@app.route('/list_space')
def list_space():
    return render_template('list_space.html')

@app.route('/list_space', methods=['POST'])
def list_new_space():
    name = request.form['name']
    description = request.form['description']
    cost = request.form['cost']
    user_id = session['user_id']
    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)
    repository.create(name,description,cost,user_id)
    return redirect("/account_page")

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
