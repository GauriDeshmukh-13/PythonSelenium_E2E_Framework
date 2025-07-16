from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from E2E_Test1.utils.E2E_util1 import BrowserTitle


class CC(BrowserTitle):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.check_btn = (By.CSS_SELECTOR, ".btn.btn-success")
        self.country_name = (By.CSS_SELECTOR, ".validate")
        self.suggest_name = (By.CSS_SELECTOR, ".suggestions")
        self.check = (By.CSS_SELECTOR, ".checkbox")
        self.purchase_btn = (By.CSS_SELECTOR, "input[class*=btn-success]")
        self.success_msg = (By.CSS_SELECTOR, ".alert")

    def checkout(self):
        self.driver.find_element(*self.check_btn).click()

    def address(self, country):
        self.driver.find_element(*self.country_name).send_keys(country)
        WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(self.suggest_name)
        )
        self.driver.find_element(*self.suggest_name).click()

    def purchase(self):
        self.driver.find_element(*self.check).click()
        self.driver.find_element(*self.purchase_btn).click()

    def validate_msg(self):
        msg = self.driver.find_element(*self.success_msg).text
        assert "Success! Thank you!" in msg, "Order Not Successful :("
