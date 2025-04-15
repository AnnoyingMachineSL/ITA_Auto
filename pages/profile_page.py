from pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.ADD_PET_BUTTON = self.page.locator('//*[@id="app"]/main/div/div/div[1]/div/div[1]/button')
        self.PET_NAME = self.page.locator('//*[@id="name"]')
        self.PET_AGE = self.page.locator('//*[@id="age"]/input')
        self.PET_TYPE = self.page.locator('//*[@id="typeSelector"]')
        self.PET_GENDER = self.page.locator('//*[@id="genderSelector"]')
        self.SUBMIT_PAGE = self.page.locator('//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')


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
        self.page.get_by_text(gender).click()

    def click_submit_button(self):
        self.SUBMIT_PAGE.click()

