from pages.base_page import BasePage
from pages.locators import PetProfileLocators
from pages.config import Commends


class PetProfilePage(BasePage):
    def go_to_details(self):
        go_to_details = self.browser.find_element(*PetProfileLocators.DETAILS)
        go_to_details.click()

    def send_commend(self):
        send_commend = self.browser.find_element(*PetProfileLocators.COMMEND_INPUT)
        send_commend.send_keys(*Commends.commend_good)

    def save_commend(self):
        save_commend = self.browser.find_element(*PetProfileLocators.SUBMIT_BTN)
        save_commend.click()
