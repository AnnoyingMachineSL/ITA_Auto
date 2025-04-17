from playwright.sync_api import expect

from pages.base_page import BasePage
from config import ProfilePageConfig


class ProfilePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.ADD_PET_BUTTON = self.page.locator('//*[@id="app"]/main/div/div/div[1]/div/div[1]/button')
        self.PET_NAME = self.page.locator('//*[@id="name"]')
        self.PET_AGE = self.page.locator('//*[@id="age"]/input')
        self.PET_TYPE = self.page.locator('//*[@id="typeSelector"]')
        self.PET_GENDER = self.page.locator('//*[@id="genderSelector"]')
        self.SUBMIT_PAGE = self.page.locator('//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')
        self.PROFILE_BUTTON = self.page.locator('//*[@id="app"]/header/div/ul/li[1]/a')
        self.PET_UNITS = self.page.locator(ProfilePageConfig.PET_UNIT)
        self.DELETE_MESSAGE = self.page.get_by_text('Pet record has been removed.')

    def click_add_pet_button(self):
        self.ADD_PET_BUTTON.click()

    def fill_name_field(self, name):
        self.PET_NAME.fill(name)

    def fill_age_field(self, age):
        self.PET_AGE.fill(age)

    def click_type_dropdown(self):
        self.PET_TYPE.click()
    def click_pet_type(self, pet_type):
        self.page.get_by_text(pet_type).click()

    def click_pet_gender_dropdown(self):
        self.PET_GENDER.click()

    def click_pet_gender(self, gender):
        self.page.get_by_text(gender).nth(0).click()

    def click_submit_button(self):
        self.SUBMIT_PAGE.click()

    def click_profile_button(self):
        self.PROFILE_BUTTON.click()

    def delete_pet_from_list(self, num):
        self.PET_UNITS.nth(num).get_by_text('Delete').click()

    def click_yes(self):
        self.page.get_by_text('Yes').click()

    def find_delete_message(self):
        expect(self.DELETE_MESSAGE).to_be_visible()


