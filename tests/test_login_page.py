import pytest
from playwright.sync_api import Playwright, expect
from pytest_bdd import given, when, then, parsers, scenarios

from pageObjects.loginPage import LoginPage

scenarios('../features/login_page.feature')
scenarios('../features/forgot_password_page.feature')


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


@given(parsers.parse('User authorizes with {user_email} and {user_password}'))
@when(parsers.parse('User authorizes with {user_email} and {user_password}'))
def user_enters_email_value(user_email, user_password, shared_data):
    on_login_page = shared_data['login_page']
    home_page = on_login_page.login_with_user_credentials(user_email, user_password)
    shared_data['home_page'] = home_page


@then('User is on the Home page')
def verify_the_greetings_message(shared_data):
    on_home_page = shared_data['home_page']
    expect(on_home_page.main_greeting_text).to_have_text('Welcome toPlextera Studio!')


@then('User is authorized')
def verify_the_greetings_message(shared_data):
    on_home_page = shared_data['home_page']
    expect(on_home_page.user_greeting_text).to_have_text("Welcome back, Alexandr!")


@when('User clicks user menu dropdown')
def open_personal_cabinet_menu(shared_data):
    on_home_page = shared_data['home_page']
    on_home_page.personal_cabinet_dropdown_menu.click()


@when('User clicks the Log Out point')
def select_log_out_point(shared_data):
    on_home_page = shared_data['home_page']
    on_home_page.log_out_menu_point.click()


@then('Plextera the Login page is successfully opened')
def login_page_is_displayed(shared_data):
    on_login_page = shared_data['login_page']
    expect(on_login_page.page_title).to_have_text("Welcome to Plextera")


@then(parsers.parse('Error message is successfully shown {error_text}'))
def check_the_error_text(error_text, shared_data):
    on_login_page = shared_data['login_page']
    expect(on_login_page.wrong_credentials_error).to_have_text(error_text)

@when('User clicks the Forgot password button')
def click_forgot_password(shared_data):
    on_login_page = shared_data['login_page']
    forgot_password_page = on_login_page.transfer_to_forgot_password_page()
    shared_data['forgot_password_page'] = forgot_password_page

@then('Plextera the Forgot password page is successfully opened')
def success_forgot_page_open(shared_data):
    on_forgot_password_page = shared_data['forgot_password_page']
    expect(on_forgot_password_page.page_title).to_have_text("Forgot password")
