from playwright.sync_api import expect
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.LOGIN_FIELD = self.page.locator('//*[@id="login"]')
        self.PASSWORD_FIELD = self.page.locator('//*[@id="password"]/input')
        self.SUBMIT_BUTTON = self.page.get_by_text('Submit')

    def fill_login_field(self, login):
        self.LOGIN_FIELD.fill(login)

    def fill_password_field(self, password):
        self.PASSWORD_FIELD.fill(password)
        self.PASSWORD_FIELD.press('Enter')

    def click_submit_button(self):
        self.SUBMIT_BUTTON.click()

    def check_profile_page(self):
        expect(self.page).to_have_url('http://34.141.58.52:8080/#/profile')