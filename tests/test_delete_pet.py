import time

from playwright.sync_api import expect
from pages.profile_page import ProfilePage
import random


class TestDeletePet:
    def test_delete_pet(self, login):
        page = ProfilePage(login)
        expect(page.PET_UNITS.nth(0)).to_be_visible()
        pets_count = page.PET_UNITS.count()
        pet_number = random.choice(range(0, pets_count))
        page.delete_pet_from_list(pet_number)
        page.click_yes()
        page.find_delete_message()





