import re
import allure
import pytest

from config import LoginPageConfig
from pages.login_page import LoginPage
import time


@allure.title('[Valid data] Login Test')
class TestLogin:
    def test_login(self, page):
        login_page = LoginPage(page)
        login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
        login_page.fill_login_field(LoginPageConfig.LOGIN)
        login_page.fill_password_field(LoginPageConfig.PASSWORD)
        login_page.press_enter_password()

@allure.title('[Invalid data] Negative Login Test')
@allure.severity(allure.severity_level.CRITICAL)
class TestLoginNegative:
    @pytest.mark.negative #Маркировка тестов. Использся pytest -m negative запустятся только тесты с маркой negative
    @pytest.mark.dependency(name='test_login_invalid_email')
    @pytest.mark.parametrize('email, password', [('a', ''), ('', ''), ('@gmail.com', 'a')])
    @allure.description('Log in with incorrect email and expect an error message')
    def test_login_invalid_email(self, page, email, password):
        login_page = LoginPage(page)
        with allure.step('Open login page'):
            login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
        with allure.step(f'Fill login field with {email}'):
            login_page.fill_login_field(email)
        with allure.step(f'Fill password field with {password}'):
            login_page.fill_password_field(password)
        with allure.step('Press Enter'):
            login_page.press_enter_password()

        if len(re.findall('.*@mail.com', email)) == 0:
            login_page.check_invalid_email()
        if len(password) == 0:
            login_page.check_password_error()


    @pytest.mark.negative
    @pytest.mark.dependency(depends='test_login_invalid_email')
    @pytest.mark.parametrize('email, password', [('a', ''), ('', ''), ('@gmail.com', 'a'), ('a@mail.com', '')])
    def test_login_invalid_data(self, page, email, password):
        login_page = LoginPage(page)
        login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
        login_page.fill_login_field(email)
        login_page.fill_password_field(password)
        login_page.press_enter_password()
        if len(re.findall('.*@mail.com', email)) == 0:
            login_page.check_invalid_email()
        if len(password) == 0:
            login_page.click_login_logo()
            login_page.check_password_error()
