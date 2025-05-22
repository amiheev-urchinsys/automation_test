from playwright.sync_api import Page

class Sidebar:
    def __init__(self, page: Page):
        self.company_selector = page.locator('.organization')
        self.workflows_point = page.locator('div[aria-label="Workflows"]')
        self.web_automations_point = page.locator('div[aria-label="Web Automations"]')
        self.documents_insights_point = page.locator('div[aria-label="Document Insights"]')
        self.sides_point = page.locator('div[aria-label="SIDES"]')
        self.datastores_point = page.locator('div[aria-label="Datastores"]')
        self.forms_point = page.locator('div[aria-label="Forms"]')
        self.personal_cabinet_dropdown_menu = page.locator('.bottom-section .name')
        self.settings_pers_cab_menu_point = page.locator('div[aria-label="Settings"]')
        self.admin_console_pers_cab_menu_point = page.locator('div[aria-label="Admin Console"]')
        self.log_out_pers_cab_menu_point = page.locator('div[aria-label="Log Out"]')
        self.toggle_button = page.locator('button[aria-label="toggle"]')
        self.logo = page.locator('.logo')

