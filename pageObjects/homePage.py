from playwright.sync_api import Page

class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.user_greeting_text = page.locator(".page-content .greeting").first



