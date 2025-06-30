from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from login_helpers import AuthHelper
from links import Links
from locators import Locators


class TestRegistration:
    def __init__(self):
        self.wait_time = 5
        self.login_url = Links.link_login_page

    def wait_for_element(self, driver, locator):
        return WebDriverWait(driver, self.wait_time).until(
            EC.visibility_of_element_located(locator)
        )

    def test_registration_success(self, driver, test_email, test_password):
        driver.get(Links.link_registration_page)
        AuthHelper.registration(driver, test_email, test_password)
        AuthHelper.confirm_registration_success(driver)
        assert driver.current_url == self.login_url

    def test_registration_invalid_password(self, driver, test_email):
        driver.get(Links.link_registration_page)
        invalid_pass = "111"
        name = "Тест"

        # Заполняем форму
        self.wait_for_element(driver, Locators.locator_name).send_keys(name)
        self.wait_for_element(driver, Locators.locator_email).send_keys(test_email)
        self.wait_for_element(driver, Locators.locator_password).send_keys(invalid_pass)
        self.wait_for_element(driver, Locators.locator_button_registration).click()

        # Проверяем ошибку
        error_message = self.wait_for_element(
            driver, TestLocators.locator_message_wrong_password
        ).text
        assert error_message == "Некорректный пароль"
