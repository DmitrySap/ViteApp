import pytest
from pages.pets_page import FindPetsPage
from pages.pet_profile_page import PetProfilePage


@pytest.mark.card_commend
class TestShowTheNumberOfDogCards:
    def test_commend(self, browser, go_to_login):
        page = FindPetsPage(browser, self)
        page.menu_page()
        page.dog_name()
        page.dog_type()
        page = PetProfilePage(browser, self)
        page.go_to_details()
        page.send_commend()
        page.save_commend()
        browser.save_screenshot(r'Z:\QAlearning\Python\Selenium_UI_Pet\results\Commend.png')
