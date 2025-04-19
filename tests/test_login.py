import re
import allure
import pytest
from config import LoginPageConfig
from pages.login_page import LoginPage


@allure.title('[Positive] Login Test')
@allure.severity(allure.severity_level.CRITICAL)
class TestLogin:
    @pytest.mark.positive  # Маркировка тестов. Использся pytest -m negative запустятся только тесты с маркой negative
    @allure.title('Login with correct data')
    @allure.description('Log like existing user with correct login/password')
    def test_login(self, page):
        login_page = LoginPage(page)

        with allure.step('Open login page'):
            login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)

        with allure.step('Fill login field'):
            login_page.fill_login_field(LoginPageConfig.LOGIN)

        with allure.step('Fill password field'):
            login_page.fill_password_field(LoginPageConfig.PASSWORD)

        with allure.step('Press Enter on password field'):
            login_page.press_enter_password()

@allure.title('[Negative] Login Test')
@allure.severity(allure.severity_level.CRITICAL)
class TestLoginNegative:
    @pytest.mark.negative #Маркировка тестов. Использся pytest -m negative запустятся только тесты с маркой negative
    @allure.title('Incorrect email format')
    @pytest.mark.dependency(name='test_login_invalid_email')
    @pytest.mark.parametrize('email, password', [('a', 'qwe123'), ('', 'qwe123'), ('@gmail.com', 'a')])
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
    @allure.title('Incorrect login/password format')
    @pytest.mark.dependency(depends='test_login_invalid_email')
    @pytest.mark.parametrize('email, password', [('a', ''), ('', ''), ('@gmail.com', 'a'), ('a@mail.com', '')])
    @allure.description('Incorrect formats of login and password for login')
    def test_login_invalid_data(self, page, email, password):
        login_page = LoginPage(page)

        with allure.step('Open login page'):
            login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)

        with allure.step(f'Fill login field with {email}'):
            login_page.fill_login_field(email)

        with allure.step(f'Fill password field with {password}'):
            login_page.fill_password_field(password)

        with allure.step('Press Enter'):
            login_page.press_enter_password()

        login_page.click_login_logo()

        if not len(re.findall('.*@mail.com', email)):
            login_page.check_invalid_email()

        if not len(password):
            login_page.check_password_error()
