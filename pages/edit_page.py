import time
from pages.base_page import BasePage
from pages.locators import EditPetLocators
from pages.config import Names, Ages


class EditPage(BasePage):
    def cat_name(self):
        time.sleep(2)
        edit_name = self.browser.find_element(*EditPetLocators.NAME_INPUT)
        edit_name.clear()
        edit_name.send_keys(*Names.cat_name)

    def cat_age(self):
        edit_age = self.browser.find_element(*EditPetLocators.AGE_INPUT)
        edit_age.clear()
        edit_age.send_keys(*Ages.cat_age)

    def cat_gender(self):
        edit_gender = self.browser.find_element(*EditPetLocators.GENDER_DROPDOWN)
        edit_gender.click()
        edit_female = self.browser.find_element(*EditPetLocators.MALE)
        edit_female.click()

    def cat_type(self):
        edit_type = self.browser.find_element(*EditPetLocators.TYPE_DROPDOWN)
        edit_type.click()
        edit_parrot = self.browser.find_element(*EditPetLocators.CAT_TYPE)
        edit_parrot.click()

    def edit_submit(self):
        edit_submit = self.browser.find_element(*EditPetLocators.SUBMIT_BTN)
        edit_submit.click()
