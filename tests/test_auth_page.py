from pages.auth_page import AuthPage
from conf import *
import time


def test_auth_page_pass(selenium):
    page = AuthPage(selenium)
    time.sleep(1)  # Задержка для учебных целей
    page.enter_email(valid_email)
    page.enter_pass(valid_pass)
    page.btn_click()

    # знак != или == будет зависеть от того, верные или неверные значения мы вводим.
    assert page.get_relative_link() == '/all_pets', 'login error'

    time.sleep(1)  # Задержка для учебных целей


def test_auth_page_fail(selenium):
    page = AuthPage(selenium)
    time.sleep(1)  # Задержка для учебных целей
    page.enter_email(invalid_email)
    page.enter_pass(invalid_pass)
    page.btn_click()

    # знак != или == будет зависеть от того, верные или неверные значения мы вводим.
    assert page.get_relative_link() != '/all_pets', 'login error'

    time.sleep(1)  # Задержка для учебных целей
