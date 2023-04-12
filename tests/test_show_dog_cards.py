import pytest
from pages.pets_page import FindPetsPage
from pages.config import LoginPageData


@pytest.mark.show_cards
class TestShowTheNumberOfDogCards:
    def test_show_dog(self, browser):
        page = FindPetsPage(browser, LoginPageData.MAIN_PAGE_URL)
        page.open()
        page.dog_name()
        page.dog_type()
        page.cards_quantity()
        browser.save_screenshot(r'Z:\QAlearning\Python\Selenium_UI_Pet\results\NumberOfDogCards.png')
