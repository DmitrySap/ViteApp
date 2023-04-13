import time

from pages.base_page import BasePage
from pages.locators import AddPetLocators
from pages.config import Names, Ages


class EditPage(BasePage):
    def cat_name_clear(self):
        edit_name = self.browser.find_element(*AddPetLocators.NAME_INPUT)
        time.sleep(1)
        edit_name.clear()

    def cat_name_input(self):
        edit_name = self.browser.find_element(*AddPetLocators.NAME_INPUT)
        edit_name.send_keys(*Names.cat_name)

    def cat_age(self):
        edit_age = self.browser.find_element(*AddPetLocators.AGE_INPUT)
        edit_age.clear()
        edit_age.send_keys(*Ages.cat_age)

    def cat_gender(self):
        edit_gender = self.browser.find_element(*AddPetLocators.GENDER_DROPDOWN)
        edit_gender.click()
        edit_female = self.browser.find_element(*AddPetLocators.MALE)
        edit_female.click()

    def cat_type(self):
        edit_type = self.browser.find_element(*AddPetLocators.TYPE_DROPDOWN)
        edit_type.click()
        edit_parrot = self.browser.find_element(*AddPetLocators.CAT_TYPE)
        edit_parrot.click()

    def edit_submit(self):
        edit_submit = self.browser.find_element(*AddPetLocators.SUBMIT_EDIT_BTN)
        edit_submit.click()
