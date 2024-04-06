from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = 'https://dev.transmatika.com/ru/log-in'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    email = browser.find_element(By.CSS_SELECTOR, "input")
    email.click()
    email.send_keys("qa@xono.one")
    assert email != "qa@xono.one", \
    f"Введенный email отличается от qa@xono.one. Ваш email - '{email}'"
    confirm_button = browser.find_element(By.CLASS_NAME, "MuiButton-containedSizeLarge")
    confirm_button.click()
finally:
    browser.quit()