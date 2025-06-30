from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from links import Links
from locators import Locators


class TestBrowseInConstructor:

    def test_browse_to_buns(self, driver, test_email, test_password):
        driver.get(Links.link_main_page)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            Locators.locator_constructor_tab_sauce)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            Locators.locator_constructor_tab_bun)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            Locators.locator_tab_active_bun))
        tab_buns = driver.find_element(*Locators.locator_tab_active_bun)
        expected_class = 'tab_tab_type_current__2BEPc'
        actual_class = tab_buns.get_attribute('class')
        assert expected_class in actual_class

    def test_browse_to_sauces(self, driver):
        driver.get(Links.link_main_page)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            Locators.locator_constructor_tab_sauce)).click()
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                Locators.locator_tab_active_sauce))
        tab_sauces = driver.find_element(
            *Locators.locator_tab_active_sauce)
        expected_class = 'tab_tab_type_current__2BEPc'
        actual_class = tab_sauces.get_attribute('class')
        assert expected_class in actual_class

    def test_navigation_to_fillings(self, driver, test_email, test_password):
        driver.get(Links.link_main_page)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            Locators.locator_constructor_tab_filling)).click()
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                Locators.locator_tab_active_filling))
        tab_fillings = driver.find_element(
            *Locators.locator_tab_active_filling)
        expected_class = 'tab_tab_type_current__2BEPc'
        actual_class = tab_fillings.get_attribute('class')
        assert expected_class in actual_class
