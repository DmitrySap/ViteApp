import pytest
import time
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from config import PagesData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.authorization
class TestLogin:

    def test_go_to_profile(self, browser):
        page = LoginPage(browser, PagesData.LOGIN_PAGE_URL)
        page.open()
        page.go_to_email()
        page.go_to_password()
        page.go_to_button()
        # Явное ожидание, ожидаем, что URL станет равен PagesData.PROFILE_PAGE_URL
        WebDriverWait(browser, 10).until(ec.url_to_be(PagesData.PROFILE_PAGE_URL))
        assert browser.current_url == PagesData.PROFILE_PAGE_URL
        browser.save_screenshot(r'result/success log in.png')

    def test_quit(self, browser, log_in):
        page = ProfilePage(browser, self)
        page.quit_from_profile()
        assert browser.current_url != PagesData.PROFILE_PAGE_URL
        browser.save_screenshot(r'result/quit.png')


@pytest.mark.authorization_error
class TestLoginError:
    def test_incorrect_password(self, browser):
        page = LoginPage(browser, PagesData.LOGIN_PAGE_URL)
        page.open()
        page.go_to_email()
        page.enter_incorrect_password()
        page.go_to_button()
        time.sleep(2)
        current_url = browser.current_url
        assert current_url == PagesData.LOGIN_PAGE_URL
        browser.save_screenshot(r'result/IncorrectPassword.png')

    def test_incorrect_email(self, browser):
        page = LoginPage(browser, PagesData.LOGIN_PAGE_URL)
        page.open()
        page.enter_incorrect_email()
        page.go_to_password()
        page.go_to_button()
        time.sleep(2)
        current_url = browser.current_url
        assert current_url == PagesData.LOGIN_PAGE_URL
        browser.save_screenshot(r'result/IncorrectEmail.png')

    def test_only_button(self, browser):
        page = LoginPage(browser, PagesData.LOGIN_PAGE_URL)
        page.open()
        page.go_to_button()
        time.sleep(2)
        current_url = browser.current_url
        assert current_url == PagesData.LOGIN_PAGE_URL
        browser.save_screenshot(r'result/OnlySubmit.png')

    def test_only_login(self, browser):
        page = LoginPage(browser, PagesData.LOGIN_PAGE_URL)
        page.open()
        page.go_to_email()
        page.go_to_button()
        time.sleep(2)
        current_url = browser.current_url
        assert current_url == PagesData.LOGIN_PAGE_URL
        browser.save_screenshot(r'result/OnlyLogin.png')

    def test_only_password(self, browser):
        page = LoginPage(browser, PagesData.LOGIN_PAGE_URL)
        page.open()
        page.go_to_password()
        page.go_to_button()
        time.sleep(2)
        current_url = browser.current_url
        assert current_url == PagesData.LOGIN_PAGE_URL
        browser.save_screenshot(r'result/OnlyPassword.png')
