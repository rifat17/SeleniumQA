import time
import unittest

import HtmlTestRunner
from selenium import webdriver
from ..pages.bikroy_home_page import BikroyHomePage
from .base_test import BaseTest


class BikroyHomepage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome('/home/hasib/PycharmProjects/SeleniumQA/drivers/chromedriver')
        self.driver.get("http://bikroy.com/en/ads/dhaka/mobiles")
        self.driver.implicitly_wait(10)

    def test_check_page_loaded(self):
        home_page = BikroyHomePage(self.driver)
        actual = home_page.check_page_loaded()
        expected = True

        self.assertEqual(expected, actual)

    def test_enter_search_kw(self):
        home_page = BikroyHomePage(self.driver)
        home_page.enter_search_kw("Laptop")

    def test_getProducts(self):
        home_page = BikroyHomePage(self.driver)
        products = home_page.get_products()

        self.assertGreater(len(products), 0)

    def test_check_nth_product_from_list(self):
        home_page = BikroyHomePage(self.driver)
        home_page.check_nth_product_from_list(5)


    def test_scroll_page(self):
        home_page = BikroyHomePage(self.driver)
        home_page.scrool_down()
        time.sleep(1)
        home_page.scrool_up()
        time.sleep(1)

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/hasib/PycharmProjects/SeleniumQA/reports'))
