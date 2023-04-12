from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from pages.config import LoginPageData


class LoginPage(BasePage):
    def go_to_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(*LoginPageData.valid_email)

    def go_to_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_password.send_keys(*LoginPageData.valid_password)

    def go_to_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_button.submit()

    def go_incorrect_password(self):
        incorrect_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        incorrect_password.send_keys(*LoginPageData.invalid_password)

    def go_incorrect_email(self):
        incorrect_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        incorrect_email.send_keys(*LoginPageData.invalid_email)
