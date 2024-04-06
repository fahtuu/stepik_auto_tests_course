from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.ID, "answer").send_keys(y)
    checkbox = browser.find_element(By.ID, "robotCheckbox").click()
    radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    submit_button = browser.find_element(By.CLASS_NAME, "btn-primary").click()
    print(browser.switch_to.alert.text.split()[-1])
finally:
    time.sleep(10)
    browser.quit()
