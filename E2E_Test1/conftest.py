import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# adding --browser_name to run from terminal
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name1", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture(scope="function")
def browser_instance(request):
    browser_name1 = request.config.getoption('browser_name1')
    if browser_name1 == "chrome":
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--start-maximized")
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--user-data-dir=/tmp/chrome-temp")
        driver = webdriver.Chrome(options=options)
    elif browser_name1 == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=firefox_options)

    driver.get('https://rahulshettyacademy.com/loginpagePractise/')
    driver.implicitly_wait(5)
    yield driver
    driver.close()
