from playwright.sync_api import Page

class SettingsPage:
    def __init__(self, page: Page):
        self.page_title = page.locator('.header__left h3')
        self.account_point = page.locator("li.tab:has(div:has-text('Account'))")
        self.notification_point = page.locator("li.tab:has(div:has-text('Notification'))")
        self.api_point = page.locator("li.tab:has(div:has-text('API'))")
        self.general_point = page.locator("li.tab:has(div:has-text('General'))")
        self.users_point = page.locator("li.tab:has(div:has-text('Users'))")
        self.billing_point = page.locator("li.tab:has(div:has-text('Billing'))")
        self.update_button_enabled = page.get_by_role("button", name="Update", disabled=False)
        self.on_account_tab = self.Account(page)
        self.on_general_tab = self.General(page)
        self.on_users_tab = self.Users(page)

    class Account:
        def __init__(self, page: Page):
            self.role_input = page.locator('input[name="role"]')
            self.email_input = page.locator('input[name="email"]')
            self.first_name = page.locator('input[name="firstName"]')
            self.last_name = page.locator('input[name="lastName"]')
            self.current_password_input = page.locator('input[name="oldPassword"]')
            self.new_password_input = page.locator('input[name="newPassword"]')
            self.confirm_password_input = page.locator('input[name="confirmNewPassword"]')

    class General:
        def __init__(self, page: Page):
            self.company_name_input = page.locator('input[name="companyName"]')
            self.company_url_input = page.locator('input[name="companyUrl"]')
            self.size_limit_input = page.locator('input[placeholder="Enter size limit"]')

    class Users:
        def __init__(self, page: Page):
            self.invite_new_user_button = page.locator('.admin__add-button')

