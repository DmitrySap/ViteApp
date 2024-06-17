from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BTN = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    REGISTER_BTN = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(2) > a > span')
    PROFILE_BTN = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span.p-menuitem-text')
    QUIT_BTN = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(2) > a')
    MENU_BTN = (By.XPATH, '//*[@id="app"]/header/div/div')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class RegisterPageLocators:
    REGISTER_EMAIL = (By.ID, "login")
    REGISTER_PASS = (By.CSS_SELECTOR, "#password > input")
    REGISTER_CONF_PASS = (By.CSS_SELECTOR, "#confirm_password > input")
    REGISTER_BTN = (By.CLASS_NAME, 'p-button-label')


class ProfileLocators:
    ADD_BTN = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-header > div > div:nth-child(1) > button')
    DELETE_PROFILE = (By.XPATH, '//*[@id="app"]/main/div/div/div[1]/div/div[2]/button/span[1]')
    EDIT_2ND_PET = (By.XPATH, '//div[2]/div/div[2]/button')
    DELETE_2ND_PET = (By.XPATH, '//div[2]/div/div[2]/button[2]')
    DELETE_2ND_PET_YES = (By.XPATH, '/html/body/div[3]/div[2]/button[2]')
    PETS_NUMBER = (By.CSS_SELECTOR, '.col-12')


class AddPetLocators:
    NAME_INPUT = (By.ID, 'name')
    AGE_INPUT = (By.CSS_SELECTOR, '#age > input')
    TYPE_DROPDOWN = (By.ID, 'typeSelector')
    PARROT_TYPE = (By.XPATH, '//li[contains(.,"parrot")]')
    CAT_TYPE = (By.XPATH, '//li[contains(.,"cat")]')
    HAMSTER_TYPE = (By.XPATH, '//li[contains(.,"hamster")]')
    GENDER_DROPDOWN = (By.ID, 'genderSelector')
    FEMALE = (By.XPATH, '//li[contains(.,"Female")]')
    MALE = (By.XPATH, '//li[contains(.,"Male")]')
    SUBMIT_EDIT_BTN = (By.XPATH, '//*[@id="app"]/main/div/form/div/div[2]/div[3]/button')
    SUBMIT_ADD_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')


class ShowDogsLocators:
    FILTER_BY_TYPE = (By.ID, 'typesSelector')
    FILTER_BY_NAME = (By.ID, 'petName')
    DOGS = (By.XPATH, '//li[contains(.,"dog")]')
    DOGS_NUMBER = (By.CSS_SELECTOR, '.col-12')


class PetProfileLocators:
    DETAILS = (By.CSS_SELECTOR, '.col-12:nth-child(1) .p-button')
    COMMEND_INPUT = (By.CSS_SELECTOR, '.ql-editor')
    SUBMIT_BTN = (By.CSS_SELECTOR, '.p-button-label')
