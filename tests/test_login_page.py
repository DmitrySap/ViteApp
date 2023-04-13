import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.config import LoginPageData
from pages.locators import LoginPageLocators


@pytest.mark.authorization
class TestLogin:

    def test_go_to_profile(self, browser):
        page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
        page.open()
        wait = WebDriverWait(browser, 10)
        wait.until(ec.visibility_of_element_located(LoginPageLocators.LOGIN_EMAIL))
        page.go_to_email()
        page.go_to_password()
        page.go_to_button()
        time.sleep(1)
        current_url = browser.current_url
        assert current_url == LoginPageData.PROFILE_PAGE_URL
        browser.save_screenshot(r'Z:\QAlearning\Python\Selenium_UI_Pet\results\ProfileEnter.png')

    def test_quit(self, browser):
        page = ProfilePage(browser, self)
        page.quit_from_profile()
        current_url = browser.current_url
        assert current_url == LoginPageData.LOGIN_PAGE_URL
        browser.save_screenshot(r'Z:\QAlearning\Python\Selenium_UI_Pet\results\ProfileQuit.png')


@pytest.mark.authorization_error
class TestLoginError:
    def test_incorrect_password(self, browser):
        page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
        page.open()
        page.go_to_email()
        page.go_incorrect_password()
        page.go_to_button()
        time.sleep(1)
        current_url = browser.current_url
        assert current_url == LoginPageData.LOGIN_PAGE_URL
        browser.save_screenshot(r'Z:\QAlearning\Python\Selenium_UI_Pet\results\IncorrectPassword.png')

    def test_incorrect_email(self, browser):
        page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
        page.open()
        page.go_incorrect_email()
        page.go_to_password()
        page.go_to_button()
        time.sleep(1)
        current_url = browser.current_url
        assert current_url == LoginPageData.LOGIN_PAGE_URL
        browser.save_screenshot(r'Z:\QAlearning\Python\Selenium_UI_Pet\results\IncorrectEmail.png')

    def test_only_button(self, browser):
        page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
        page.open()
        page.go_to_button()
        time.sleep(1)
        current_url = browser.current_url
        assert current_url == LoginPageData.LOGIN_PAGE_URL
        browser.save_screenshot(r'Z:\QAlearning\Python\Selenium_UI_Pet\results\OnlySubmit.png')

    def test_only_login(self, browser):
        page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
        page.open()
        page.go_to_email()
        page.go_to_button()
        time.sleep(1)
        current_url = browser.current_url
        assert current_url == LoginPageData.LOGIN_PAGE_URL
        browser.save_screenshot(r'Z:\QAlearning\Python\Selenium_UI_Pet\results\OnlyLogin.png')

    def test_only_password(self, browser):
        page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
        page.open()
        page.go_to_password()
        page.go_to_button()
        time.sleep(1)
        current_url = browser.current_url
        assert current_url == LoginPageData.LOGIN_PAGE_URL
        browser.save_screenshot(r'Z:\QAlearning\Python\Selenium_UI_Pet\results\OnlyPassword.png')
