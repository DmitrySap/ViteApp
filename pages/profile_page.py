from pages.base_page import BasePage
from locators import ProfileLocators, MainPageLocators


class ProfilePage(BasePage):
    def edit_pet(self):
        edit_pet = self.browser.find_element(*ProfileLocators.EDIT_2ND_PET)
        edit_pet.click()

    def add_pet(self):
        add_pet = self.browser.find_element(*ProfileLocators.ADD_BTN)
        add_pet.click()

    def delete_pet(self):
        delete_pet = self.browser.find_element(*ProfileLocators.DELETE_2ND_PET)
        delete_pet.click()

    def delete_pet_yes(self):
        delete_pet_yes = self.browser.find_element(*ProfileLocators.DELETE_2ND_PET_YES)
        delete_pet_yes.click()

    def quit_from_profile(self):
        quit_from_profile = self.browser.find_element(*MainPageLocators.QUIT_BTN)
        quit_from_profile.click()

    def go_to_profile(self):
        go_to_profile = self.browser.find_element(*MainPageLocators.PROFILE_BTN)
        go_to_profile.click()

    def cards_quantity(self):
        pets = self.browser.find_elements(*ProfileLocators.PETS_NUMBER)
        assert len(pets) == 1, f'настоящее количество карточек = {len(pets)}'