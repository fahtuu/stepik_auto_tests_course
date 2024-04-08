import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "Chrome":
        print("\nstart Chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "Firefox":
        print("\nstart Firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be Chrome or Firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
