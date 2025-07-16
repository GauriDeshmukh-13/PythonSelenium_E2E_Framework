import json

import pytest

from E2E_Test1.PageObjects1.LoginPage1 import LoginPage

json_data = "C:\\Users\\Dell\\PycharmProjects\\MyFirstFramework_Selenium_Python\\E2E_Test1\\Data1\\E2E_data.json"
with open(json_data) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


@pytest.mark.parametrize("test_item", test_list)
def test_e2e(browser_instance, test_item):
    driver = browser_instance
    login_page = LoginPage(driver)
    print(login_page.get_title())
    shop_page = login_page.login(test_item["userEmail"], test_item["userPwd"])
    print(shop_page.get_title())
    shop_page.click_shop()
    checkout_page = shop_page.select_product(test_item["Product"])
    print(checkout_page.get_title())
    checkout_page.checkout()
    checkout_page.address(test_item["Delivery_Address"])
    checkout_page.purchase()
    checkout_page.validate_msg()
