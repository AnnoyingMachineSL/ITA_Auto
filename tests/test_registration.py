import time

import allure
import playwright
import pytest
from playwright.sync_api import sync_playwright
from client import Client
from models.pet_models import LoginModel, LoginResponseModel
from utils import generator
from pages.registration_page import RegistrationPage


@allure.title('[Positive Test] Registration')
@allure.severity(allure.severity_level.CRITICAL)
class TestRegistration:
    @pytest.mark.positive
    @allure.title('Correct data for registration')
    @allure.description('Registration using correct format of login and password')
    def test_registration(self, open_chrome, page):
        page = RegistrationPage(open_chrome)

        with allure.step('Open registration page'):
            page.open_page(page.REGISTRATION_PAGE_URL)

        random_email = generator.random_email()
        print(random_email)
        with allure.step(f'Fill email field by {random_email}'):
            page.fill_login_field(generator.random_email())

        password = generator.random_password()
        print(password)
        with allure.step(f'Fill password and confirm password field by {password}'):
            page.fill_password_field(password)
            page.fill_confirm_field(password)

        with allure.step('Click on registration logo'):
            page.click_registration_logo()

        with allure.step('Click Submit button'):
            page.click_submit_button()

        with allure.step('Check the correct redirection after registration'):
            page.check_profile_page()
            page.click_main_page_button()

        with allure.step('[POST /login] Authorization'):
            Client().login(request=LoginModel(email=random_email, password=password),
                                                    expected_model=LoginResponseModel(), status_code=200)


@allure.title('[Negative Test] Registration')
@allure.severity(allure.severity_level.CRITICAL)
class TestRegistrationNegative:

    @pytest.mark.negative
    @allure.title('Incorrect email format')
    @pytest.mark.dependency(name='test_registration_invalid_email')
    @pytest.mark.parametrize('email, password', [('a', 'qwe123'), ('', 'qwe123'), ('@gmail.com', 'qwe123')])
    @allure.description('Registration with incorrect email and expect an error message')
    def test_registration_invalid_email_format(self, page, email, password):
        page = RegistrationPage(page)

        with allure.step('Open registration page'):
            page.open_page(page.REGISTRATION_PAGE_URL)

        with allure.step(f'Fill email field by {email}'):
            page.fill_login_field(email)

        with allure.step(f'Fill password and confirm password field by {password}'):
            page.fill_password_field(password)
            page.fill_confirm_field(password)

        with allure.step('Click on registration logo'):
            page.click_registration_logo()

        with allure.step('Click Submit button'):
            page.click_submit_button()

        with allure.step('Check the error message'):
            page.check_email_error_message()

    @pytest.mark.negative
    @allure.title('Incorrect password/confirm_password')
    @pytest.mark.dependency(depends='test_registration_invalid_email')
    @pytest.mark.parametrize('password, confirm_password', [('', ''), ('qwe', '123'), ('qwe', ''), ('', 'qwe')])
    @allure.description('Incorrect password/confirm_password pairs and data format')
    def test_registration_invalid_data_format(self, page, password, confirm_password):
        page = RegistrationPage(page)

        with allure.step('Open registration page'):
            page.open_page(page.REGISTRATION_PAGE_URL)

        with allure.step(f'Fill email field by [qwe@mail.com]'):
            page.fill_login_field('qwe@mail.com')

        with allure.step(f'Fill password field by {password}'):
            page.fill_password_field(password)

        with allure.step(f'Fill confirm_password field by {confirm_password}'):
            page.fill_confirm_field(confirm_password)

        with allure.step('Click on registration logo'):
            page.click_registration_logo()

        with allure.step('Click Submit button'):
            page.click_submit_button()

        if not len(password) and not len(confirm_password):
            page.check_confirm_password_error_message()
            page.check_password_error_message()

        if len(password) and len(confirm_password) and password != confirm_password:
            page.check_something_went_wrong_error_message()

        if not len(confirm_password):
            page.check_confirm_password_error_message()

        if not len(password):
            page.check_password_error_message()
