from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from login_helpers import AuthHelper
from links import Links
from locators import Locators


class TestRegistration:

    def test_registration_success(self, driver, test_email, test_password):
        driver.get(Links.link_registration_page)
        AuthHelper.registration(driver, test_email, test_password, )
        AuthHelper.confirm_registration_success(driver)
        current_url = driver.current_url
        expected_result = Links.link_login_page
        assert expected_result == current_url


    def test_registration_invalid_password(self, driver, test_email):
        driver.get(Links.link_registration_page)
        invalid_pass = "111"
        driver.find_element(*Locators.locator_name).send_keys("Тест")
        driver.find_element(*Locators.locator_email).send_keys(test_email)
        driver.find_element(
            *Locators.locator_password).send_keys(invalid_pass)
        driver.find_element(*Locators.locator_button_registration).click()
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                Locators. locator_message_wrong_password)).text
        expected_error_msg = "Некорректный пароль"
        assert expected_error_msg == error_message
