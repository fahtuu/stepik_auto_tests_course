from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    number1 = browser.find_element(By.ID, "num1")
    number2 = browser.find_element(By.ID, "num2")
    num1 = number1.text
    num2 = number2.text
    summ = int(num1) + int(num2)
    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_value(str(summ))
    button = browser.find_element(By.CLASS_NAME, "btn").click()
finally:
    time.sleep(10)
    browser.quit()
