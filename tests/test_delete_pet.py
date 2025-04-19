import time

import allure
import pytest
from playwright.sync_api import expect
from pages.profile_page import ProfilePage
import random

@allure.title('Positive Delete Per')
@allure.severity(allure.severity_level.NORMAL)
class TestDeletePet:

    @pytest.mark.positive
    @allure.title('Delete pet from profile page')
    def test_delete_pet(self, login):
        page = ProfilePage(login)

        with allure.step('Wait all pet units'):
            page.wait_pet_unit()

        with allure.step('Calculate pet count'):
            pets_count = page.PET_UNITS.count()

        with allure.step('Random choice a pet'):
            pet_number = random.choice(range(0, pets_count))

        with allure.step('Delete selected pet'):
            page.delete_pet_from_list(pet_number)

        with allure.step('Click yes on pop-up'):
            page.click_yes()

        with allure.step('Check the delete message'):
            page.find_delete_message()





