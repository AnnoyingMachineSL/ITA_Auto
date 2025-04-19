import allure
import pytest
import generator
from pages.profile_page import ProfilePage
import time


@allure.title('Add pet test')
@allure.severity(allure.severity_level.CRITICAL)
class TestAddPet:

    @pytest.mark.positive
    @allure.title('Add pet by correct data')
    @pytest.mark.parametrize('pet_type, age, gender', [('dog', '1', 'male'), ('cat', '2', 'female'),
                                                       ('reptile', '3', 'male'), ('hamster', '1', 'female'),
                                                       ('parrot', '2', 'male')])
    def test_add_pet(self, login, pet_type, age, gender):
        page = ProfilePage(login)

        with allure.step('Click Add Pet button'):
            page.click_add_pet_button()

        with allure.step('Fill pet name field'):
            page.fill_name_field(generator.random_name())

        with allure.step(f'Fill pet age field by {age}'):
            page.fill_age_field(age)

        with allure.step(f'Click on pet type dropdown'):
            page.click_type_dropdown()

        with allure.step(f'Fill pet type field by {pet_type}'):
            page.click_pet_type(pet_type)

        with allure.step(f'Click on pet gender dropdown'):
            page.click_pet_gender_dropdown()

        with allure.step(f'Fill pet gender field by {gender}'):
            page.click_pet_gender(gender)

        with allure.step('Click submit button'):
            page.click_submit_button()

        with allure.step('Click Profile button'):
            page.click_profile_button()
            time.sleep(0.1)

@allure.title('Negative Add Pet Test')
@allure.severity(allure.severity_level.CRITICAL)
class TestAddPetNegative:

    @pytest.mark.negative
    @allure.title('Incorrect name and type data')
    @pytest.mark.parametrize('name, pet_type', [('', 'dog'), ('bober', ''), ('', '')])
    @allure.description('Registration with incorrect email and expect an error message')
    def test_add_pet_empty_fields(self, login, name, pet_type):
        page = ProfilePage(login)

        with allure.step('Click Add Pet button'):
            page.click_add_pet_button()

        if not len(pet_type) and len(name):
            with allure.step(f'Fill pet name field by {name}'):
                page.fill_name_field(name)

            with allure.step('Click submit button'):
                page.click_submit_button()

            with allure.step('Check pet type error message'):
                page.check_pet_type_error_message()

            with allure.step('Click Profile button'):
                page.click_profile_button()

        if not len(name) and len(pet_type):
            with allure.step(f'Click on pet type dropdown'):
                page.click_type_dropdown()

            with allure.step(f'Fill pet type field by {pet_type}'):
                page.click_pet_type(pet_type)

            with allure.step('Click submit button'):
                page.click_submit_button()

            with allure.step('Check name error message'):
                page.check_name_error_message()

            with allure.step('Click Profile button'):
                page.click_profile_button()

        if not len(name) and not len(pet_type):
            with allure.step('Click submit button'):
                page.click_submit_button()

            with allure.step('Check name error message'):
                page.check_name_error_message()

            with allure.step('Check pet type error message'):
                page.check_pet_type_error_message()

            with allure.step('Click Profile button'):
                page.click_profile_button()
