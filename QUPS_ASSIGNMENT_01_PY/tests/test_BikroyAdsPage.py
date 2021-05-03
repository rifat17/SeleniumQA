import time
import unittest

import pytest
from selenium import webdriver

from QUPS_ASSIGNMENT_01_PY.src.pages.bikroy_ads_page import BikroyAdsPage


class Test_BikroyAdsPage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.get("http://bikroy.com/en/ads/")
        self.driver.implicitly_wait(1)

    def test_find_copyright_text(self):
        ads_page = BikroyAdsPage(self.driver)

        ads_page.scroll_down()
        copyright_text = ads_page.find_copyright().text
        self.assertIsNotNone(copyright_text)
        self.assertIn('copyright', copyright_text.lower())

    def test_find_MORE_from_BIKROY(self):
        ads_page = BikroyAdsPage(self.driver)

        links = ads_page.find_MORE_from_BIKROY()

        for link in links:
            self.driver.get(link)
            title = self.driver.title
            print("Visitin {}".format(title))
            self.assertIsNotNone(title)
            time.sleep(1)

    def test_find_HELP_n_SUPPORT(self):
        ads_page = BikroyAdsPage(self.driver)

        links = ads_page.find_HELP_n_SUPPORT()

        for link in links:
            self.driver.get(link)
            title = self.driver.title
            print("Visitin {}".format(title))
            self.assertIsNotNone(title)
            time.sleep(1)

    def test_find_FOLLOW_BIKROY(self):
        ads_page = BikroyAdsPage(self.driver)

        links = ads_page.find_FOLLOW_BIKROY()

        for link in links:
            self.driver.get(link)
            title = self.driver.title
            print("Visitin {}".format(title))
            self.assertIsNotNone(title)
            time.sleep(1)

    def test_find_ABOUT_BIKROY(self):
        ads_page = BikroyAdsPage(self.driver)

        links = ads_page.find_ABOUT_BIKROY()

        for link in links:
            self.driver.get(link)
            title = self.driver.title
            print("Visitin {}".format(title))
            self.assertIsNotNone(title)
            time.sleep(1)

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()


# @pytest.fixture()
# def chrome_driver(request):
#     chrome_driver = webdriver.Chrome()
#     chrome_driver.implicitly_wait(5)
#     yield chrome_driver
#     chrome_driver.close()


if __name__ == '__main__':
    unittest.main()
