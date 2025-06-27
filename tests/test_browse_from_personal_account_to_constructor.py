from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from links import (Links)
from locators import Locators

class TestBrowseToConstructor:

    def wait_and_click(self, driver, locator, timeout=5):
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def verify_url(self, driver, expected_url, timeout=10):
        WebDriverWait(driver, timeout).until(
            EC.url_to_be(expected_url)
        )
        assert driver.current_url == expected_url


    def test_browse_from_account_to_constructor(self, driver, authorized_user):
        self.wait_and_click(driver, Locators.locator_button_personal_account)
        self.verify_url(driver, Links.link_personal_account_page)
        self.wait_and_click(driver, Locators.locator_button_constructor)
        self.verify_url(driver, Links.link_main_page)


    def test_browse_from_account_to_constructor_logo(self, driver, authorized_user):
        self.wait_and_click(driver, Locators.locator_button_personal_account)
        self.verify_url(driver, Links.link_personal_account_page)
        self.wait_and_click(driver, Locators.locator_button_logo)
        self.verify_url(driver, Links.link_main_page)