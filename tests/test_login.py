from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from login_helpers import AuthHelper
from links import Links
from locators import Locators

class TestLogin:

    def test_login_main_page(self, driver, registered_user):
        test_email, test_password = registered_user
        driver.get(Links.link_main_page)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            Locators.locator_login_button)).click()
        AuthHelper.login(driver, test_email, test_password)
        WebDriverWait(driver, 10).until(EC.url_to_be(Links.link_main_page))
        assert driver.current_url == Links.link_main_page


    def test_login_personal_account_button(self, driver, registered_user):
        test_email, test_password = registered_user
        driver.get(Links.link_main_page)
        WebDriverWait(
            driver, 10).until(
            EC.element_to_be_clickable(
                Locators.locator_button_personal_account)).click()
        AuthHelper.login(driver, test_email, test_password)
        WebDriverWait(driver, 10).until(EC.url_to_be(Links.link_main_page))
        assert driver.current_url == Links.link_main_page

    def test_login_registration_link(self, driver, registered_user):
        test_mail, test_pass = registered_user
        driver.get(Links.link_registration_page)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            Locators.locator_login_link)).click()
        AuthHelper.login(driver, test_mail, test_pass)
        WebDriverWait(driver, 10).until(EC.url_to_be(Links.link_main_page))
        assert driver.current_url == Links.link_main_page

    def test_login_forgot_password_link(self, driver, registered_user):
        test_mail, test_pass = registered_user
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                Locators.locator_login_link)).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                Locators.locator_login_link)).click()
        AuthHelper.login(driver, test_mail, test_pass)
        WebDriverWait(driver, 10).until(EC.url_to_be(Links.link_main_page))
        assert driver.current_url == Links.link_main_page
