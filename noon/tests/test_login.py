from time import sleep

import allure


@allure.feature('Авторизация')
@allure.story('Корректный логин')
def test_correct_login(login_page):
    login_page.open_base_page()
    sleep(5)
    login_page.open_login_page()
    sleep(5)
    login_page.enter_email(email="perevalovi.v@gmail.com")
    sleep(5)
    login_page.click_button_continue()
    sleep(5)

@allure.feature('Авторизация')
@allure.story('Не корректный логин')
def test_incorrect_login(login_page):
    login_page.open_base_page()
    sleep(5)
    login_page.open_login_page()
    sleep(5)
    login_page.enter_email(email="perevalovi.v")
    sleep(5)
    login_page.click_button_continue()
    sleep(5)
    login_page.should_see_invalid_email_error()
    sleep(5)