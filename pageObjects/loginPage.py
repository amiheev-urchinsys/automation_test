from playwright.sync_api import Page
from pageObjects.homePage import HomePage


class LoginPage:

    def __init__(self, page: Page):
        """
        Initializes the LoginPage object with web element locators.

        :param page: Playwright Page object representing the browser tab or frame.
        """
        self.page = page
        self.email_input = page.locator('#email')
        self.password_input = page.locator('#password')
        self.login_button = page.get_by_role("button", name="Log in")
        self.page_title = page.locator('.MuiContainer-root h1')

    def login_with_user_credentials(self, user_email, user_password):
        """
        Performs login action using the provided user credentials.

        :param user_email: Email address to input in the Email address field in the login form
        :param user_password: Password to input in the Password field in the login form
        :return: Instance of HomePage object, assuming login is successful
        """
        self.email_input.fill(user_email)
        self.password_input.fill(user_password)
        self.login_button.click()

        home_page = HomePage(self.page)
        return home_page
