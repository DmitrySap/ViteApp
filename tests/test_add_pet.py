import time
import pytest
from pages.add_page import AddPage
from pages.profile_page import ProfilePage
from pages.edit_page import EditPage
from locators import ProfileLocators


@pytest.mark.add_pet
class TestAddEditDeletePet:
    def test_add_pet(self, browser, log_in):
        page = ProfilePage(browser, self)
        page.add_pet()
        page = AddPage(browser, self)
        page.add_name()
        page.add_age()
        page.add_gender()
        page.add_type()
        page.submit_add()
        time.sleep(1)
        page = ProfilePage(browser, self)
        page.go_to_profile()
        browser.refresh()
        pets = browser.find_elements(*ProfileLocators.PETS_NUMBER)
        assert len(pets) == 2, f'настоящее количество карточек = {len(pets)}'
        browser.save_screenshot(r'result/AddPet.png')

    def test_edit_to_cat(self, browser, log_in):
        page = ProfilePage(browser, self)
        page.edit_pet()
        page = EditPage(browser, self)
        time.sleep(1)
        page.cat_name_clear()
        page.cat_age()
        page.cat_name_input()
        page.cat_gender()
        page.cat_type()
        page.edit_submit()
        time.sleep(1)
        browser.save_screenshot(r'result/EditToCat.png')

    def test_delete_2nd_pet(self, browser, log_in):
        page = ProfilePage(browser, self)
        page.delete_pet()
        page.delete_pet_yes()
        browser.refresh()
        time.sleep(1)
        page.cards_quantity()
        browser.save_screenshot(r'result/DeletePet.png')
