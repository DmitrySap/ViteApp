import time
import pytest
import requests
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.config import LoginPageData
from pages.locators import LoginPageLocators


test_data = [('hgdaw@mail.ru', 'SAdf'), ('rif@mail.ru', 'Urtuk!'), ('rif@mail.ru', 'qQwer')]


# @pytest.mark.authorization('email', ['hgdaw@mail.ru', 'rif@mail.ru'])
# def test_login(browser, email):
#         page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
#         page.open()
#         wait = WebDriverWait(browser, 10)
#         wait.until(ec.visibility_of_element_located(LoginPageLocators.LOGIN_EMAIL))
#         login_email = browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
#         login_email.send_keys(email)
#         page.go_to_password()
#         page.go_to_button()
#         time.sleep(1)
#         browser.save_screenshot(r'Z:\QAlearning\Python\Selenium_UI_Pet\results\ProfileEnter.png')
#         response = requests.get('http://34.141.58.52:8080/#/profile')
#         print(response)
#         assert response.status_code == 200


@pytest.mark.parametrize("email", ['hgdaw@mail.ru', 'rif@mail.ru'])
def test_login(browser, email):
    link = 'http://34.141.58.52:8080/#/login'
    browser.get(link)
    login_email = browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
    login_email.send_keys(email)
    time.sleep(1)
    page = LoginPage(browser, link)
    page.go_to_password()
    time.sleep(1)
    page.go_to_button()
    time.sleep(1)
    response = requests.get('http://34.141.58.52:8080/#/profile')
    print(response)
    assert response.status_code == 200
