import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
from password import *

@pytest.mark.parametrize("url", [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
def test_login(browser, url):
    link = url
    browser.get(link)
    browser.implicitly_wait(15)
    ## Нажатие на кнопку авторизации в шапке сайта
    login = browser.find_element(By.CLASS_NAME, "navbar__auth_login").click()
    ## Поиск и ввод в поле email
    input_email = browser.find_element(By.ID, "id_login_email")
    input_email.send_keys(email)
    ## Поиск и ввод в поле  password
    password_input = browser.find_element(By.ID, "id_login_password")
    password_input.send_keys(password)
    ## Нажати на кнопку "Войти"
    confirm = browser.find_element(By.CLASS_NAME, "sign-form__btn").click()
    #ok_button = browser.find_element(By.LINK_TEXT, "OK").click()
    time.sleep(5)
    ## Ввод answer и отправка результата
    answer = math.log(int(time.time()))
    input_answer = browser.find_element(By.CLASS_NAME, "ember-text-area")
    input_answer.send_keys(answer)

    ## ТУТ Я ЗАДАЛ ОЖИДАНИЕ НА 5 СЕКУНД, ЧТОБЫ ПРОВЕРИТЬ ЧТО КНОПКА ДОСТУПНА ДЛЯ НАЖАТИЯ
    confirm = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    #confirm = browser.find_element(By.CLASS_NAME, "submit-submission")
    confirm.click()
    alert_correct = browser.find_element(By.CLASS_NAME,"smart-hints__hint")
    alert_text = alert_correct.text
    assert alert_text == "Correct!"
    ## Cброс введенного ранее значения, чтобы не отправить тот же результат
    reset_button = browser.find_element(By.CLASS_NAME, "again-btn").click()

