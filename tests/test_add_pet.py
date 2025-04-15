import generator
from pages.profile_page import ProfilePage
import time


class TestAddPet:

    def test_add_pet(self, page, login):
        page = ProfilePage(page)
        page.click_add_pet_button()
        page.fill_name_field(generator.random_name())
        page.fill_age_field(generator.random_age())
        page.click_type_dropdown()
        page.click_pet_type(generator.random_type())
        page.click_pet_gender_dropdown()
        page.click_pet_gender(generator.random_gender())
        page.click_submit_button()
        page.click_profile_button()