from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from links import Links
from locators import Locators

class TestLogout:
    def __init__(self):
        self.wait_time = 5
        self.login_url = Links.link_login_page

    def wait_and_click_logout(self, driver, locator):
        WebDriverWait(driver, self.wait_time).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def test_logout_personal_account(self, driver, authorized_user):
        self.wait_and_click_logout(driver, Locators.locator_button_personal_account)
        self.wait_and_click_logout(driver, Locators.locator_button_logout)
        WebDriverWait(driver, 10).until(
            EC.url_to_be(self.login_url)
        )
        assert driver.current_url == self.login_url
