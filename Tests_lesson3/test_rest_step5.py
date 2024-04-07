import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
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
def test_reset_exercise(browser,url):
    link = url
    browser.get(link)
    login = browser.find_element(By.CLASS_NAME, "navbar__auth_login").click()
    input_email = browser.find_element(By.ID, "id_login_email")
    input_email.send_keys(email)
    password_input = browser.find_element(By.ID, "id_login_password")
    password_input.send_keys(password)
    confirm = browser.find_element(By.CLASS_NAME, "sign-form__btn").click()
    reset_button = browser.find_element(By.CLASS_NAME, "again-btn white").click()
    ok_button = browser.find_element(By.XPATH, '//button[text()="OK"]')
    ok_button.click()
    time.sleep(1)