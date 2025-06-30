from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from login_helpers import AuthHelper
from links import Links
from locators import Locators

class TestLogin:
    self.wait_time = 10
    self.main_page_url = Links.link_main_page

    def wait_and_click_login(self, driver, locator):
        WebDriverWait(driver, self.wait_time).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def perform_login(self, driver, registered_user):
        generated_mail, generated_password = registered_user
        AuthHelper.login(driver, generated_mail, generated_password)
        self.wait_for_main_page(driver)
        self.assert_main_page(driver)

    def wait_for_main_page(self, driver):
        WebDriverWait(driver, self.wait_time).until(
            EC.url_to_be(self.main_page_url)
        )

    def assert_main_page(self, driver):
        assert driver.current_url == self.main_page_url

    def test_login_main_page(self, driver, registered_user):
        driver.get(Links.link_main_page)
        self.wait_and_click_login(driver, Locators.locator_login_button)
        self.perform_login(driver, registered_user)

    def test_login_personal_account_button(self, driver, registered_user):
        driver.get(Links.link_main_page)
        self.wait_and_click_login(driver, Locators.locator_button_personal_account)
        self.perform_login(driver, registered_user)

    def test_login_registration_link(self, driver, registered_user):
        driver.get(Links.link_registration_page)
        self.wait_and_click_login(driver, Locators.locator_login_link)
        self.perform_login(driver, registered_user)

    def test_login_forgot_password_link(self, driver, registered_user):
        self.wait_and_click_login(driver, Locators.locator_forgot_password)
        self.wait_and_click_login(driver, Locators.locator_login_link)
        self.perform_login(driver, registered_user)
