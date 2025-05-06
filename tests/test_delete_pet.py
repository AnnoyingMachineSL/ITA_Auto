import time

import allure
import pytest
from playwright.sync_api import expect

from client import Client
from config import LoginPageConfig, LoginPageSecond
from models.pet_models import LoginModel, LoginResponseModel
from pages.profile_page import ProfilePage
import random


@allure.title('[Positive test] Delete Pet')
@allure.severity(allure.severity_level.NORMAL)
class TestDeletePet:

    @pytest.mark.positive
    @allure.title('Delete pet from profile page')
    @pytest.mark.parametrize('email', [LoginPageConfig.LOGIN])
    @pytest.mark.parametrize('password', [LoginPageSecond.PASSWORD])
    def test_delete_pet(self, login, email: str, password: str):
        page = ProfilePage(login)

        with allure.step('Wait all pet units'):
            page.wait_pet_unit()

        with allure.step('Calculate pet count'):
            pets_count = page.PET_UNITS.count()

        with allure.step('Random choice a pet'):
            pet_number = random.choice(range(0, pets_count))

        with allure.step('Get pet id'):
            page.edit_pet_from_list(pet_number)
            page.reload_page()
            pet_id = int(page.get_url().split('/')[-1])
            page.get_back()

        with allure.step('Delete selected pet'):
            page.delete_pet_from_list(pet_number)

        with allure.step('Click yes on pop-up'):
            page.click_yes()

        with allure.step('Check the delete message'):
            page.find_delete_message()

        with allure.step('[POST /login] Authorization'):
            authorization_response = Client().login(request=LoginModel(email=email, password=password),
                                                    expected_model=LoginResponseModel())

        with allure.step('Create API request to check new pet'):
            headers = dict(Authorization=f'Bearer {authorization_response.token}')
            Client().get_pet(pet_id=pet_id, headers=headers, status_code=404)
