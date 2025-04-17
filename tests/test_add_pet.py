import pytest
from playwright.sync_api import expect

import generator
from pages.profile_page import ProfilePage
import time


class TestAddPet:
    @pytest.mark.parametrize('pet_type', ['dog', 'cat', 'reptile', 'hamster', 'parrot'])
    @pytest.mark.parametrize('age', ['2'])
    @pytest.mark.parametrize('gender', ['male', 'female'])
    def test_add_pet(self, login, pet_type, age, gender):
        page = ProfilePage(login)
        page.click_add_pet_button()
        page.fill_name_field(generator.random_name())
        page.fill_age_field(age)
        page.click_type_dropdown()
        page.click_pet_type(pet_type)
        page.click_pet_gender_dropdown()
        page.click_pet_gender(gender)
        page.click_submit_button()
        expect(page.PROFILE_BUTTON).to_be_visible()
        page.click_profile_button()
        time.sleep(1)