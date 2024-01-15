from playwright.sync_api import Playwright, Page, expect

# Tests for your routes go here

# """
# We can render the index page
# """
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")

#     # We look at the <p> tag
#     strong_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     expect(strong_tag).to_have_text("This is the homepage.")

"""
Get home
Returns page with title
"""
def test_request_returns_homepage(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/")
    strong_tag = page.locator("h1")
    expect(strong_tag).to_have_text("Welcome to MakersB&B")

"""
Homepage has user sign up UI
"""
def test_request_homepage_has_correct_ui(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/")
    email_input = page.locator('input[name="email"]')
    assert email_input.is_visible()
    password_input = page.locator('input[name="password"]')
    assert password_input.is_visible()
    password_confirmation_input = page.locator('input[name="password_confirmation"]')
    assert password_confirmation_input.is_visible()
    submit_button = page.locator('input[type="submit"]')
    assert submit_button.is_visible()

"""
Log-in page has user log-in UI
"""
def test_request_login_page_has_correct_ui(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/login")
    email_input = page.locator('input[name="email"]')
    assert email_input.is_visible()
    password_input = page.locator('input[name="password"]')
    assert password_input.is_visible()
    submit_button = page.locator('input[type="submit"]')
    assert submit_button.is_visible()

"""
When log-in link is clicked
Takes us to log in page
"""
def test_log_in_link_takes_us_to_login_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/")
    page.click("text='Log In'")
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text("Log in to Makers B&B")

"""
Test creates new user
"""
def test_create_new_user(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/")
    page.fill("input[name='user_name']", "Raymond Holt")
    page.fill("input[name='email']", "testemail4@example.com")
    page.fill("input[name='password']", "test-password-4")
    page.fill("input[name='password_confirmation']", "test-password-4")
    page.get_by_role("button", name="Sign Up").click()
    expect(page).to_have_url(f"http://{test_web_address}/login")

def test_correct_login(page,test_web_address,db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name='email']", "testemail1@example.com")
    page.fill("input[name='password']", "test-password-1")
    page.get_by_role("button", name="Log In").click()
    expect(page).to_have_url(f"http://{test_web_address}/account_page")

def test_incorrect_login(page,test_web_address,db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name='email']", "asdfg")
    page.fill("input[name='password']", "jkjkj")
    page.get_by_role("button", name="Log In").click()
    expect(page).to_have_url(f"http://{test_web_address}/login")

def test_signout_button(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name='email']", "testemail1@example.com")
    page.fill("input[name='password']", "test-password-1")
    page.get_by_role("button", name="Log In").click()
    expect(page).to_have_url(f"http://{test_web_address}/account_page")
    page.click("text='Sign Out'")
    expect(page).to_have_url(f"http://{test_web_address}/")