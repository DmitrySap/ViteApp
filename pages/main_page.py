from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_BTN)
        login_link.click()

    def go_to_register_page(self):
        registration_link = self.browser.find_element(*MainPageLocators.REGISTER_BTN)
        registration_link.click()
