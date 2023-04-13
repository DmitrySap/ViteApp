import pytest
from pages.pets_page import FindPetsPage
from pages.pet_profile_page import PetProfilePage
from pages.locators import ShowDogsLocators, PetProfileLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.card_commend
class TestShowTheNumberOfDogCards:
    def test_commend(self, browser, go_to_login):
        page = FindPetsPage(browser, self)
        page.menu_page()
        wait = WebDriverWait(browser, 10)
        wait.until(ec.visibility_of_element_located(ShowDogsLocators.FILTER_BY_NAME))
        page.dog_name()
        page.dog_type()
        page = PetProfilePage(browser, self)
        wait.until(ec.visibility_of_element_located(PetProfileLocators.DETAILS))
        page.go_to_details()
        wait.until(ec.visibility_of_element_located(PetProfileLocators.COMMEND_INPUT))
        page.send_commend()
        page.save_commend()
        browser.save_screenshot(r'Z:\QAlearning\Python\Selenium_UI_Pet\results\Commend.png')
