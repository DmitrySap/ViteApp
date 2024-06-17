import pytest
from pages.main_page import MainPage
from pages.pets_page import FindPetsPage
from pages.pet_profile_page import PetProfilePage


@pytest.mark.card_commend
class TestShowTheNumberOfDogCards:
    def test_commend(self, browser, log_in):
        page = MainPage(browser, self)
        page.go_to_main_page()
        page = FindPetsPage(browser, self)
        page.dog_name()
        page.dog_type()
        page = PetProfilePage(browser, self)
        page.go_to_details()
        page.send_commend()
        page.save_commend()
        browser.save_screenshot(r'result/commend.png')
