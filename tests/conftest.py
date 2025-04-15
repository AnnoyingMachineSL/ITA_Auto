import pytest

from config import LoginPageConfig
from pages.login_page import LoginPage

@pytest.fixture()
def login(page):
    login_page = LoginPage(page)
    login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
    login_page.fill_password_field(LoginPageConfig.PASSWORD)
    login_page.fill_login_field(LoginPageConfig.LOGIN)
    login_page.click_submit_button()