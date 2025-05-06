from playwright.sync_api import expect

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.REGISTRATION_PAGE_URL = 'http://34.141.58.52:8080/#/register'
        self.LOGIN_FIELD = page.locator('//*[@id="login"]')
        self.PASSWORD_FIELD = page.locator('//*[@id="password"]/input')
        self.CONFIRM_PASSWORD = page.locator('//*[@id="confirm_password"]/input')
        self.LOGIN_FIELD_ERROR_MESSAGE = page.get_by_text('This field is email')
        self.PASSWORD_FIELD_ERROR_MESSAGE = page.locator('//*[@id="pv_id_2_content"]/div/form/div[2]/div[2]')
        self.CONFIRM_PASSWORD_ERROR_MESSAGE = page.locator('//*[@id="pv_id_2_content"]/div/form/div[3]/div[2]')
        self.SOMETHING_WENT_WRONG_MESSAGE = page.locator('//*[@id="pv_id_2_content"]/div/div/div')
        self.REGISTRATION_LOGO = page.locator('//*[@id="app"]/main/fieldset/legend')
        self.SUBMIT_BUTTON = page.locator('//*[@id="pv_id_2_content"]/div/form/div[4]/button')
        self.PROFILE_BUTTON = page.get_by_text('Profile')
        self.MAIN_PAGE_BUTTON = page.locator('//*[@id="app"]/header/div/div/img')

    def fill_login_field(self, login):
        self.LOGIN_FIELD.fill(login)

    def fill_password_field(self, password):
        self.PASSWORD_FIELD.fill(password)

    def fill_confirm_field(self, password):
        self.CONFIRM_PASSWORD.fill(password)

    def check_profile_page(self):
        expect(self.page).to_have_url('http://34.141.58.52:8080/#/profile')

    def check_email_error_message(self):
        expect(self.LOGIN_FIELD_ERROR_MESSAGE).to_be_visible()

    def check_password_error_message(self):
        expect(self.PASSWORD_FIELD_ERROR_MESSAGE).to_be_visible()

    def check_confirm_password_error_message(self):
        expect(self.CONFIRM_PASSWORD_ERROR_MESSAGE).to_be_visible()

    def check_something_went_wrong_error_message(self):
        expect(self.SOMETHING_WENT_WRONG_MESSAGE).to_be_visible()

    def click_registration_logo(self):
        self.REGISTRATION_LOGO.click()

    def click_submit_button(self):
        self.SUBMIT_BUTTON.click()

    def click_profile_button(self):
        self.PROFILE_BUTTON.click()

    def click_main_page_button(self):
        self.MAIN_PAGE_BUTTON.click()
