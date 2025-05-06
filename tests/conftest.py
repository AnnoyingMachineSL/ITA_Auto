import playwright
import pytest

from config import LoginPageConfig
from pages.login_page import LoginPage


@pytest.fixture(scope='session')
def login(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
    login_page.fill_password_field(LoginPageConfig.PASSWORD)
    login_page.fill_login_field(LoginPageConfig.LOGIN)
    login_page.click_submit_button()
    return page


@pytest.fixture()
def open_chrome(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    return page