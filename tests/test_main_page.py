import pytest
from pages.main_page import MainPage
from pages.config import LoginPageData


@pytest.mark.login_page
class TestLoginAndRegister:

    def test_go_to_login_page(self, browser):
        page = MainPage(browser, LoginPageData.MAIN_PAGE_URL)
        page.open()
        page.go_to_login_page()
        current_url = browser.current_url
        assert current_url == LoginPageData.LOGIN_PAGE_URL
        browser.save_screenshot(r'Z:\QAlearning\Python\Selenium_UI_Pet\results\LoginPage.png')

    def test_go_to_register_page(self, browser):
        page = MainPage(browser, self)
        page.go_to_register_page()
        current_url = browser.current_url
        assert current_url == LoginPageData.REGISTER_PAGE_URL
        browser.save_screenshot(r'Z:\QAlearning\Python\Selenium_UI_Pet\results\RegisterPage.png')
