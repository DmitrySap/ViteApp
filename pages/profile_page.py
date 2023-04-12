from pages.base_page import BasePage
from pages.locators import ProfileLocators, MainPageLocators


class ProfilePage(BasePage):
    def delete_profile(self):
        delete = self.browser.find_element(*ProfileLocators.DELETE_PROFILE)
        delete.click()

    def edit_pet(self):
        edit_pet = self.browser.find_element(*ProfileLocators.EDIT_3RD_PET)
        edit_pet.click()

    def add_pet(self):
        add_pet = self.browser.find_element(*ProfileLocators.ADD_BTN)
        add_pet.click()

    def delete_pet(self):
        delete_pet = self.browser.find_element(*ProfileLocators.DELETE_3RD_PET)
        delete_pet.click()

    def delete_pet_yes(self):
        delete_pet_yes = self.browser.find_element(*ProfileLocators.DELETE_3RD_PET_YES)
        delete_pet_yes.click()

    def quit_from_profile(self):
        quit_from_profile = self.browser.find_element(*MainPageLocators.QUIT_BTN)
        quit_from_profile.click()

    def go_to_profile(self):
        go_to_profile = self.browser.find_element(*MainPageLocators.PROFILE_BTN)
        go_to_profile.click()
