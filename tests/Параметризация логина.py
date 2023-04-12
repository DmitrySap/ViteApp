import time
import pytest
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.config import LoginPageData


@pytest.mark.authorization('email', ['rif@mail.ru', 'QQWWEE@mail.ru'])
def test_go_to_profile(browser, email):
        page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
        page.open()
        page.go_to_email(email)
        page.go_to_password()
        page.go_to_button()
        time.sleep(1)
        browser.save_screenshot(r'Z:\QAlearning\Python\Selenium_UI_Pet\results\ProfileEnter.png')
