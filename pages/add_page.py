import time

from pages.base_page import BasePage
from pages.locators import AddPetLocators
from pages.config import Names, Ages


class AddPage(BasePage):

    def add_name(self):
        time.sleep(1)
        add_name = self.browser.find_element(*AddPetLocators.NAME_INPUT)
        add_name.send_keys(*Names.hamster_name)

    def add_age(self):
        add_age = self.browser.find_element(*AddPetLocators.AGE_INPUT)
        add_age.send_keys(*Ages.hamster_age)

    def add_gender(self):
        add_gender = self.browser.find_element(*AddPetLocators.GENDER_DROPDOWN)
        add_gender.click()
        add_male = self.browser.find_element(*AddPetLocators.MALE)
        add_male.click()

    def add_type(self):
        add_type = self.browser.find_element(*AddPetLocators.TYPE_DROPDOWN)
        add_type.click()
        hamster = self.browser.find_element(*AddPetLocators.HAMSTER_TYPE)
        hamster.click()

    def submit_add(self):
        submit_btn = self.browser.find_element(*AddPetLocators.SUBMIT_BTN)
        submit_btn.submit()
