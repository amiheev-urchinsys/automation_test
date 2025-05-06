from playwright.sync_api import Page

class HomePage:

    def __init__(self, page: Page):
        """
        Initializes the HomePage object with web element locators.

        :param page: Playwright Page object representing the browser tab or frame.
        """
        self.page = page
        self.user_greeting_text = page.locator(".page-content .greeting").first
        self.main_greeting_text = page.locator('.content .greeting')


