from playwright.sync_api import expect
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.LOGIN_FIELD = self.page.locator('//*[@id="login"]')
        self.PASSWORD_FIELD = self.page.locator('//*[@id="password"]/input')
        self.SUBMIT_BUTTON = self.page.get_by_text('Submit')
        self.FIELD_IS_EMAIL_MESSAGE = self.page.get_by_text('This field is email')
        self.FIELD_IS_PASSWORD_MESSAGE = self.page.get_by_text('This field is required')
        self.LOGIN_LOGO = self.page.locator('//*[@id="app"]/main/fieldset/legend')

    def fill_login_field(self, login):
        self.LOGIN_FIELD.fill(login)

    def fill_password_field(self, password):
        self.PASSWORD_FIELD.fill(password)

    def press_enter_password(self):
        self.PASSWORD_FIELD.press('Enter')

    def click_submit_button(self):
        self.SUBMIT_BUTTON.click()

    def check_profile_page(self):
        expect(self.page).to_have_url('http://34.141.58.52:8080/#/profile')

    def check_password_error(self):
       expect(self.FIELD_IS_PASSWORD_MESSAGE).to_be_visible()

    def check_invalid_email(self):
        expect(self.FIELD_IS_EMAIL_MESSAGE).to_be_visible()

    def click_login_logo(self):
        self.LOGIN_LOGO.click()