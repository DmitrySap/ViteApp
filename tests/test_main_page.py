import pytest
from pages.main_page import MainPage
from config import PagesData


@pytest.mark.login_page
class TestLoginAndRegister:

    def test_go_to_login_page(self, browser):
        page = MainPage(browser, PagesData.MAIN_PAGE_URL)
        page.open()
        page.go_to_login_page()
        current_url = browser.current_url
        assert current_url == PagesData.LOGIN_PAGE_URL
        browser.save_screenshot(r'result/login.png')

    def test_go_to_register_page(self, browser):
        page = MainPage(browser, PagesData.MAIN_PAGE_URL)
        page.open()
        page.go_to_register_page()
        current_url = browser.current_url
        assert current_url == PagesData.REGISTER_PAGE_URL
        browser.save_screenshot(r'result/register.png')

    def test_go_to_main_page(self, browser):
        page = MainPage(browser, PagesData.LOGIN_PAGE_URL)
        page.open()
        page.go_to_main_page()
        current_url = browser.current_url
        assert current_url == PagesData.MAIN_PAGE_URL
        browser.save_screenshot(r'result/main page.png')