import pytest
from pages.pets_page import FindPetsPage
from config import PagesData


@pytest.mark.show_cards
class TestShowTheNumberOfDogCards:
    def test_show_dog(self, browser):
        page = FindPetsPage(browser, PagesData.MAIN_PAGE_URL)
        page.open()
        page.dog_name()
        page.dog_type()
        page.cards_quantity()
        browser.save_screenshot(r'result/NumberOfDogCards.png')
