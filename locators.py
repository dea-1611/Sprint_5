from selenium.webdriver.common.by import By


class Locators:
    locator_name = (By.XPATH, ".//*[text()='Имя']/following-sibling::input")                            # Поле ввода имени

    locator_email = (By.XPATH, ".//*[text()='Email']/following-sibling::input")                         # Поле ввода email

    locator_password = (By.XPATH, ".//*[text()='Пароль']/following-sibling::input")                     # Поле ввода пароля

    locator_login_button = (By.XPATH, '//*[contains(@class, "button_button_type_primary")]')            # Кнопка "Войти в аккаунт" на главной странице
                                                                                                        # и "Войти" в ЛК

    locator_login_link = (By.XPATH, '//*[contains(@class, "Auth_link")]')                               # Ссылка "Войти" на страницах регистрации
                                                                                                        # и восстановления пароля

    locator_button_registration = (By.XPATH, '//*[contains(@class, "button_button_type_primary")]')     # Кнопка "Зарегистрироваться" в форме регистрации

    locator_button_personal_account = (By.XPATH, "// *[contains(text(), 'Личный Кабинет')]")            # кнопка "Личный Кабинет"

    locator_button_constructor = (By.XPATH, "// *[contains(text(), 'Конструктор')]")                    # кнопка "Конструктор"

    locator_button_logout = (By.XPATH, "//*[contains(@class, 'Account_button')]")                       # кнопка "Выход" в ЛК
    locator_button_logo = (By.XPATH, "//*[contains(@class, 'AppHeader_header__logo')]")                 # Логотип в шапке

                                                                                                        # Вкладки конструктора
    locator_constructor_tab_bun = (By.XPATH, "*//span[contains(text(), 'Булки')]")
    locator_constructor_tab_sauce = (By.XPATH, "*//span[contains(text(), 'Соусы')]")
    locator_constructor_tab_filling = (By.XPATH, "*//span[contains(text(), 'Начинки')]")

                                                                                                        # Активные вкладки
    locator_tab_active_bun = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') "
        "and span/text()='Булки']")
    locator_tab_active_sauce = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') "
        "and span/text()='Соусы']")
    locator_tab_active_filling = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc') "
        "and span/text()='Начинки']")

    locator_message_wrong_password = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")         # Сообщение о некорректном пароле
    locator_forgot_password = (By.XPATH, "//a[text()='Восстановить пароль']")                           # ссылка Восстановить пароль
