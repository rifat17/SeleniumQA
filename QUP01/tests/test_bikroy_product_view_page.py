import time
import unittest

import HtmlTestRunner
from selenium import webdriver
from ..pages.bikroy_product_view_page import BikroyProductViewPage
from .base_test import BaseTest


class BikroyProductViewepage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome('/home/hasib/PycharmProjects/SeleniumQA/drivers/chromedriver')
        self.driver.get("http://bikroy.com/en/ad/xiaomi-redmi-8-4-64-used-for-sale-dhaka-673")
        self.driver.implicitly_wait(10)

    def test_check_page_loaded(self):
        product_page = BikroyProductViewPage(self.driver)
        actual = product_page.check_page_loaded()
        expected = True

        self.assertEqual(expected, actual)

    def test_get_cheapest_product_from_ads(self):
        driver = self.driver
        product_page = BikroyProductViewPage(driver)
        cheapest_product = product_page.get_cheapest_product_from_ads()
        cheapest_product.click()

        product_page = BikroyProductViewPage(driver)
        products = product_page.get_cheapest_product_info()

        for i in range(0, len(products), 2):
            attr = products[i].text
            value = products[i + 1].text
            print("{} : {}".format(attr, value))

            self.assertIsNotNone(value, "{} is None".format(attr))

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/hasib/PycharmProjects/SeleniumQA/reports'))
