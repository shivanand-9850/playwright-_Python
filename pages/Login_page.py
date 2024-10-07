from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.contact_number_input = self.page.locator("input[placeholder='Enter Contact Number']")
        self.password_input = self.page.locator("input[placeholder='Password']")
        self.login_button = self.page.get_by_role("button", name="Login")
        self.continue_button = self.page.get_by_role("button", name="Continue")
        self.show_password_button = self.page.get_by_role("img", name="Show Password")

    def navigate(self):
        self.page.goto("https://mysitebook.io/")

    def close_popup(self):
        self.page.locator("#close img").click()

    def login(self, contact_number: str, password: str):
        self.page.goto("https://app.mysitebook.io/app/auth/signin")
        self.contact_number_input.fill(contact_number)
        self.continue_button.click()
        self.password_input.fill(password)
        self.show_password_button.click()
        self.password_input.fill("Test@12345")  # For testing new password flow

        self.login_button.click()

