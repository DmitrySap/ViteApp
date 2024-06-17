from pages.base_page import BasePage
from locators import LoginPageLocators
from config import ProfileData


class LoginPage(BasePage):
    def go_to_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(*ProfileData.valid_email)

    def go_to_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_password.send_keys(*ProfileData.valid_password)

    def go_to_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_button.submit()

    def enter_incorrect_password(self):
        incorrect_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        incorrect_password.send_keys(*ProfileData.invalid_password)

    def enter_incorrect_email(self):
        incorrect_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        incorrect_email.send_keys(*ProfileData.invalid_email)
