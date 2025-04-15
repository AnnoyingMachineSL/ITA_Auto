from playwright.sync_api import expect
import generator
from pages.registration_page import RegistrationPage
import time


class TestRegistration:

    def test_registration(self, page):
        page = RegistrationPage(page)
        page.open_page(page.REGISTRATION_PAGE_URL)
        page.fill_login_field(generator.random_email())
        password = generator.random_password()
        page.fill_password_field(password)
        page.fill_confirm_field(password)
        page.check_profile_page()
        time.sleep(2)
        #expect(page).to_have_url('http://34.141.58.52:8080/#/profile')
