from config import LoginPageConfig
from pages.login_page import LoginPage
import time


class TestLogin:
    def test_login(self, page):
        login_page = LoginPage(page)
        login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
        login_page.fill_login_field(LoginPageConfig.LOGIN)
        login_page.fill_password_field(LoginPageConfig.PASSWORD)
        time.sleep(2)