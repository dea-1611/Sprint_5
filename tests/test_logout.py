from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from links import Links
from locators import Locators

class TestLogout:

    def test_logout_personal_account(self, driver, authorized_user):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            Locators.locator_button_personal_account)).click()
        WebDriverWait(
            driver, 10).until(
            EC.element_to_be_clickable(
                Locators.locator_button_logout)).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(Links.link_login_page))
        assert driver.current_url == Links.link_login_page
