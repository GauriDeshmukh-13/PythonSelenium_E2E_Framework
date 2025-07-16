from selenium.webdriver.common.by import By

from E2E_Test1.PageObjects1.ShopPage1 import Shop
from E2E_Test1.utils.E2E_util1 import BrowserTitle


class LoginPage(BrowserTitle):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username = (By.ID, "username")
        self.password = (By.NAME, "password")
        self.signin = (By.ID, "signInBtn")

    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signin).click()
        shop_page = Shop(self.driver)
        return shop_page
