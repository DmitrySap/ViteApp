import pytest
from pages.pets_page import FindPetsPage
from pages.config import LoginPageData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.show_cards
class TestShowTheNumberOfDogCards:
    def test_show_dog(self, browser):
        page = FindPetsPage(browser, LoginPageData.MAIN_PAGE_URL)
        page.open()
        wait = WebDriverWait(browser, 10)
        wait.until(ec.visibility_of_element_located((By.ID, 'petName')))
        page.dog_name()
        page.dog_type()
        page.cards_quantity()
        browser.save_screenshot(r'Z:\QAlearning\Python\Selenium_UI_Pet\results\NumberOfDogCards.png')
