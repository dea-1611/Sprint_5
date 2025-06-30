from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from links import Links
from locators import Locators


class TestBrowseInConstructor:
    def __init__(self):
        self.wait_time = 5
        self.active_class = 'tab_tab_type_current__2BEPc'

    def wait_and_click_constructor(self, driver, locator):
        WebDriverWait(driver, self.wait_time).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def check_active_tab(self, driver, locator, tab_name):
        WebDriverWait(driver, self.wait_time).until(
            EC.presence_of_element_located(locator)
        )
        tab = driver.find_element(*locator)
        actual_class = tab.get_attribute('class')
        assert self.active_class in actual_class

    def test_browse_to_buns(self, driver, test_email, test_password):
        driver.get(Links.link_main_page)
        self.wait_and_click_constructor(driver, Locators.locator_constructor_tab_sauce)
        self.wait_and_click_constructor(driver, Locators.locator_constructor_tab_bun)
        self.check_active_tab(driver, Locators.locator_tab_active_bun, 'Булки')

    def test_browse_to_sauces(self, driver):
        driver.get(Links.)
        self.wait_and_click_constructor(driver, Locators.locator_constructor_tab_sauce)
        self.check_active_tab(driver, Locators.locator_tab_active_sauce, 'Соусы')

    def test_browse_to_fillings(self, driver, test_email, test_password):
        driver.get(Links.link_main_page)
        self.wait_and_click_constructor(driver, Locators.locator_constructor_tab_filling)
        self.check_active_tab(driver, Locators.locator_tab_active_filling, 'Начинки')
