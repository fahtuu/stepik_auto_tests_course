import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = 'https://suninjuly.github.io/file_input.html'
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt.txt"
file_path = os.path.join(current_dir, file_name)
#file_path = "C:\\Users\\fahtu\\Documents\\python_project\\Project\\file_example.txt.txt"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.NAME, "firstname").send_keys("Имя")
    last_name = browser.find_element(By.NAME, "lastname").send_keys("Фамилия")
    email = browser.find_element(By.NAME, "email").send_keys("test@gmail.com")
    #print(current_dir, file_name, file_path, sep="\n", end= " |||")
    send_file = browser.find_element(By.NAME, "file").send_keys(file_path)
    submit_button = browser.find_element(By.CLASS_NAME,"btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()

