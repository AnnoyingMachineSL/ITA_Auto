from pages.profile_page import ProfilePage
import time


class TestDeletePet:
    def test_delete_pet(self, page, login):
        page = ProfilePage(page)
        print(666)
        print(page.DELETE_BUTTON)
        print(page.DELETE_BUTTON.count())
        page.DELETE_BUTTON.nth(0).click()
        time.sleep(2)




