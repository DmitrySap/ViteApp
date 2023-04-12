from pages.base_page import BasePage
from pages.locators import ShowDogsLocators, MainPageLocators
from pages.config import Names


class FindPetsPage(BasePage):
    def menu_page(self):
        menu = self.browser.find_element(*MainPageLocators.MENU_BTN)
        menu.click()

    def dog_type(self):
        types = self.browser.find_element(*ShowDogsLocators.FILTER_BY_TYPE)
        types.click()
        dog_type = self.browser.find_element(*ShowDogsLocators.DOGS)
        dog_type.click()

    def dog_name(self):
        name = self.browser.find_element(*ShowDogsLocators.FILTER_BY_NAME)
        name.clear()
        name.send_keys(*Names.dog_name)

    def cards_quantity(self):
        rif_cards = self.browser.find_elements(*ShowDogsLocators.DOGS_NUMBER)
        assert len(rif_cards) == 2, f'настоящее количество карточек = {len(rif_cards)}'
