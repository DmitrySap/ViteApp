import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.config import LoginPageData


@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture()
def go_to_login(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.go_to_email()
    page.go_to_password()
    page.go_to_button()
