import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from config import PagesData


@pytest.fixture()
def browser():
    browser = webdriver.Firefox()
    browser.maximize_window()  # окно браузера на всю страницу
    browser.implicitly_wait(10)  # вызвал неявное ожидание
    yield browser
    browser.quit()


@pytest.fixture()
def log_in(browser):
    link = PagesData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.go_to_email()
    page.go_to_password()
    page.go_to_button()
