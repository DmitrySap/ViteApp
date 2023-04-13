from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.locators import AddPetLocators
import time
import pytest

from pages.add_page import AddPage
from pages.profile_page import ProfilePage
from pages.edit_page import EditPage


@pytest.mark.add_pet
class TestAddEditDeletePet:
    def test_add_button(self, browser, go_to_login):
        page = ProfilePage(browser, self)
        page.add_pet()

    def test_add_pet(self, browser):
        page = AddPage(browser, self)
        wait = WebDriverWait(browser, 10)
        wait.until(ec.visibility_of_element_located(AddPetLocators.NAME_INPUT))
        page.add_name()
        page.add_age()
        page.add_gender()
        page.add_type()
        page.submit_add()
        page = ProfilePage(browser, self)
        page.go_to_profile()

    def test_edit_to_cat(self, browser):
        page = ProfilePage(browser, self)
        page.edit_pet()
        page = EditPage(browser, self)
        page.cat_name()
        page.cat_age()
        page.cat_gender()
        page.cat_type()
        page.edit_submit()
        time.sleep(1)
        browser.save_screenshot(r'Z:\QAlearning\Python\Selenium_UI_Pet\results\EditToCat.png')

    def test_delete_3rd_pet(self, browser):
        page = ProfilePage(browser, self)
        page.delete_pet()
        page.delete_pet_yes()
