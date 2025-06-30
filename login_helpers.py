from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from links import Links
from generator import Generator
from locators import Locators


class AuthHelper:
    # Метод для логина пользователя
    @staticmethod
    def login(driver, email, password):
        # Заполняем форму входа
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            Locators.EMAIL_LOCATOR))
        driver.find_element(*Locators.EMAIL_LOCATOR).send_keys(email)
        driver.find_element(*Locators.PASSWORD_LOCATOR).send_keys(password)
        # Нажимаем кнопку "Войти"
        driver.find_element(*Locators.LOGIN_BUTTON_LOCATOR).click()

    # Метод для регистрации пользователя
    @staticmethod
    def registration(driver, email, password, name="Тест"):
        def fill_registration_form(driver, email, password, name):
            # Заполняем форму регистрации
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(Locators.locator_name))
            driver.find_element(*Locators.locator_name).send_keys(name)
            driver.find_element(*Locators.locator_email).send_keys(email)
            driver.find_element(
                *Locators.locator_password).send_keys(password)
            # Нажимаем кнопку "Зарегистрироваться"
            driver.find_element(*Locators.locator_button_registration).click()

        fill_registration_form(driver, email, password, name)

        # Проверка, что пользователь уже существует
        while AuthHelper.is_user_already_exists(driver):
            email = Generator.generate_email()  # Генерируем новый email
            driver.refresh()  # Обновляем страницу
            fill_registration_form(driver, email, password, name)

    # Проверка успешности редиректа после логина
    @staticmethod
    def confirm_login_success(driver):
        # Проверяем, что мы на главной странице
        WebDriverWait(driver, 10).until(EC.url_to_be(
            Links.link_main_page))

    # Проверка успешности редиректа после регистрации
    @staticmethod
    def confirm_registration_success(driver):
        # Проверяем, что мы на странице логина
        WebDriverWait(driver, 10).until(EC.url_to_be(
            Links.link_login_page))
