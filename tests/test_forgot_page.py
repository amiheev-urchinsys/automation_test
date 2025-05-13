import pytest
from playwright.sync_api import Playwright, expect
from pytest_bdd import given, when, then, parsers, scenarios

from pageObjects.forgotPasswordPage import ForgotPasswordPage

scenarios('../features/forgot_password_page.feature')

@pytest.fixture
def shared_data():
    return {}

@given('User is on the Forgot page')
def open_forgot_password_page(playwright: Playwright, shared_data):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://studio.dev.plextera.com/login/forgot")
    forgot_password_page = ForgotPasswordPage(page)
    shared_data['forgot_password_page'] = forgot_password_page

@when('User clicks the Back to log in button')
def click_the_forgot_password_button(shared_data):
    on_forgot_password_page = shared_data['forgot_password_page']
    login_page = on_forgot_password_page.return_to_login_page()

    shared_data['login_page'] = login_page


