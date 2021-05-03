import time
import unittest

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from QUPS_ASSIGNMENT_01_PY.src.pages.bikroy_product_page import BikroyProductPage


class Test_BikroyProductPage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome('chromedriver')
        # self.driver.get("http://bikroy.com/en/ad/jira-pani-for-sale-dhaka-1/")
        self.driver.get("https://bikroy.com/en/ad/xiaomi-redmi-8-2019-used-for-sale-rajshahi-8")
        self.driver.implicitly_wait(5)

    def test_get_posted_on(self):
        product_page = BikroyProductPage(self.driver)

        actual = product_page.get_posted_on()
        self.assertIsNotNone(actual)

    def test_get_description(self):
        product_page = BikroyProductPage(self.driver)

        actual = product_page.get_description()
        self.assertIsNotNone(actual)


    def test_get_seller_mobile_button(self):
        product_page = BikroyProductPage(self.driver)
        button = product_page.get_seller_mobile_button()
        if not button:
            pytest.skip("No mobile number provided.")
            # self.skipTest("No mobile number provided.")
        self.assertIsNotNone(button)
        button.click()
        mobile_number = product_page.get_seller_mobile_number()
        self.assertIsNotNone(mobile_number)

        # with pytest.raises(Exception) as exinfo:
        #
        #     button = product_page.get_seller_mobile_button()
        #     self.assertIsNotNone(button)
        #     button.click()
        #     mobile_number = product_page.get_seller_mobile_number()
        #     self.assertIsNotNone(mobile_number)
        # assert str(exinfo.value) == 'Message: No Mobile Number Provided.\n'


    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
