from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "https://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    check = browser.find_element(By.CLASS_NAME, "form-check-label")
    check.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    button = browser.find_element(By.CLASS_NAME, "btn-default")
    button.click()
finally:
    time.sleep(10)
    browser.quit()