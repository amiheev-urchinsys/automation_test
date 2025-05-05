import pytest
from playwright.sync_api import Playwright, expect
from pytest_bdd import given, when, then, parsers, scenarios

from pageObjects.loginPage import LoginPage

scenarios('../features/authorization.feature')

@pytest.fixture
def shared_data():
    return {}

@given('User is on the login page')
def open_login_page(playwright: Playwright, shared_data):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://studio.dev.plextera.com/")
    login_page = LoginPage(page)
    shared_data['login_page'] = login_page

@when(parsers.parse('User authorizes with {user_email} and {user_password}'))
def user_enters_email_value(user_email, user_password, shared_data):
    on_login_page = shared_data['login_page']
    home_page = on_login_page.login_with_user_credentials(user_email, user_password)
    shared_data['home_page'] = home_page

@then('User is on the Home page and the greetings text is visible')
def verify_the_greetings_message(shared_data):
    on_home_page = shared_data['home_page']
    expect(on_home_page.user_greeting_text).to_have_text("Welcome back, Alexandr!")
