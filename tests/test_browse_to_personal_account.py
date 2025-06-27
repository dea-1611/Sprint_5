from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from links import Links
from locators import Locators

class TestBrowseToPersonalAccount:
    def test_browse_to_personal_account(self, driver, authorized_user):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(Locators.locator_button_personal_account)).click()

        wait.until(EC.url_contains(Links.link_personal_account))
        assert driver.current_url == Links.link_personal_account