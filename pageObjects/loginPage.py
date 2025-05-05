from playwright.sync_api import Page

from pageObjects.homePage import HomePage


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator('#email')
        self.password_input = page.locator('#password')
        self.login_button = page.get_by_role("button", name="Log in")

    def login_with_user_credentials(self, user_email, user_password):
        """
        Reads user credentials from a JSON file and performs user authentication.
        """
        self.email_input.fill(user_email)
        self.password_input.fill(user_password)
        self.login_button.click()

        home_page = HomePage(self.page)
        return home_page
