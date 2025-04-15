import generator
from pages.profile_page import ProfilePage
import time


class TestAddPet:

    def test_add_pet(self, page, login):
        page = ProfilePage(page)
        page.click_add_pet_button()
        page.fill_name_field(generator.random_name())
        page.fill_age_field("2")
        page.click_type_dropdown()
        page.click_pet_type('dog')
        page.click_pet_gender_dropdown()
        page.click_pet_gender('Female')
        page.click_submit_button()
        time.sleep(2)