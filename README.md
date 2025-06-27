# Sprint_5

UI-тестирование сайта Stellar Burgers.

locators.py — содержит локаторы для всех элементов интерфейса.
links.py — содержит URL-адреса используемых страниц.
login_helpers.py — содержит вспомогательные функции для авторизации.
generator.py - содержит вспомогательные функии генерации данных регистрации.
conftest.py - содержит фикстуры.

## Регистрация

Успешная регистрация test_registration_success. Проверяет регистрацию с валидными данными (имя, email в формате логин@домен, пароль не менее 6 символов).

Некорректный пароль test_registration_invalid_password. Проверяет, что при вводе недопустимого пароля появляется сообщение об ошибке.

## Вход в аккаунт c главной страницы по кнопке «Войти в аккаунт»
test_login_main_page

## Вход в аккаунт через кнопку "Личный кабинет"
test_login_personal_account_button

## Вход в аккаунт через форму регистрации
test_login_registration_link

## Вход в аккаунт через восстановление пароля
test_login_forgot_password_link

## Переход в "Личный кабинет"
test_browse_to_personal_account

## Переход из «Личного кабинета» в "Конструктор"
По кнопке «Конструктор»: test_browse_from_account_to_constructor
По клику на логотип: test_browse_from_account_to_constructor_logo

## Выход из аккаунта
test_logout_personal_account

## Переход к разделу "Соусы" в "Конструкторе"
test_browse_to_sauces()

## Переход к разделу «Булки» в "Конструкторе"
test_browse_to_buns()
Проверяет переход к разделу «Булки».

## Переход к разделу «Начинки» в "Конструкторе" 
test_browse_to_fillings
