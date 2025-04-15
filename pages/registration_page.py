from playwright.sync_api import expect

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.REGISTRATION_PAGE_URL = 'http://34.141.58.52:8080/#/register'
        self.LOGIN_FIELD = page.locator('//*[@id="login"]')
        self.PASSWORD_FIELD = page.locator('//*[@id="password"]/input')
        self.CONFIRM_PASSWORD = page.locator('//*[@id="confirm_password"]/input')


    def fill_login_field(self, login):
        self.LOGIN_FIELD.fill(login)

    def fill_password_field(self, password):
        self.PASSWORD_FIELD.fill(password)

    def fill_confirm_field(self, password):
        self.CONFIRM_PASSWORD.fill(password)
        self.CONFIRM_PASSWORD.press('Enter')

    def check_profile_page(self):
        expect(self.page).to_have_url('http://34.141.58.52:8080/#/profile')


#page.locator('//*[@id="password"]/input').fill('qwe123')
# page.locator('//*[@id="confirm_password"]/input').fill('qwe123')
# page.locator('//*[@id="confirm_password"]/input').press('Enter')
# expect(page).to_have_url('http://34.141.58.52:8080/#/profile')
