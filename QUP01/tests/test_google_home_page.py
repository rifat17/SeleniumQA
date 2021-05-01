import time
import unittest

import HtmlTestRunner
from selenium import webdriver
from ..pages.google_home_page import GoogleHomePage
from .base_test import BaseTest


class GoogleHomepage(BaseTest):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome('/home/hasib/PycharmProjects/SeleniumQA/drivers/chromedriver')
        self.driver.get("http://google.com")
        self.driver.implicitly_wait(10)

    def test_check_page_loaded(self):
        home_page = GoogleHomePage(self.driver)
        actual = home_page.check_page_loaded()
        expected = True

        self.assertEqual(actual, expected)

    def test_enter_search_kw(self):
        home_page = GoogleHomePage(self.driver)
        home_page.enter_search_kw("bikroy")

    def test_get_search_suggestions(self):
        home_page = GoogleHomePage(self.driver)
        home_page.enter_search_kw("bikroy")
        suggestion_text = home_page.get_search_suggestion_text()

        self.assertTrue(suggestion_text)

        home_page.click_a_suggestion(suggestion_text)

    def test_scroll_page(self):
        home_page = GoogleHomePage(self.driver)
        home_page.enter_search_kw("bikroy")
        suggestion_text = home_page.get_search_suggestion_text()
        home_page.click_a_suggestion(suggestion_text)
        home_page.scrool_down()
        time.sleep(1)
        home_page.scrool_up()
        time.sleep(1)

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/hasib/PycharmProjects/SeleniumQA/reports'))
