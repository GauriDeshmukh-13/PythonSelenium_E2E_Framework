from selenium.webdriver.common.by import By

from E2E_Test1.PageObjects1.checkout_confirm1 import CC
from E2E_Test1.utils.E2E_util1 import BrowserTitle


class Shop(BrowserTitle):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop = (By.CSS_SELECTOR, "a[href*='shop']")
        self.products = (By.XPATH, "//div[@class='card h-100']")
        self.checkout = (By.CSS_SELECTOR, ".nav-link.btn")

    def click_shop(self):
        self.driver.find_element(*self.shop).click()

    def select_product(self, product_name):
        products = self.driver.find_elements(*self.products)
        for p in products:
            p_name = p.find_element(By.XPATH, "div/h4/a").text
            if p_name == product_name:
                p.find_element(By.XPATH, "//div[@class='card h-100']/div/button").click()
        self.driver.find_element(*self.checkout).click()
        checkout_page = CC(self.driver)
        return checkout_page
