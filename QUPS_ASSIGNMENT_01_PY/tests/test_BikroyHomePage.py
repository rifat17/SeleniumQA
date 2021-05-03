import unittest

import pytest
from selenium import webdriver

from QUPS_ASSIGNMENT_01_PY.src.pages.bikroy_city_page import BikroyCityPage
from QUPS_ASSIGNMENT_01_PY.src.pages.bikroy_home_page import BikroyHomePage
from QUPS_ASSIGNMENT_01_PY.src.pages.bikroy_product_page import BikroyProductPage


class Test_BikroyHomePage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.get("http://bikroy.com/en/")
        self.driver.implicitly_wait(5)

    def test_case_01(self):
        home_page = BikroyHomePage(self.driver)
        home_page.scroll_down()
        actual = home_page.find_copyright().text
        expected = "Copyright © Saltside Technologies"
        self.assertEqual(expected, actual)

        post_ad = home_page.find_POST_YOUR_AD()
        self.assertIsNotNone(post_ad.text)
        self.assertIn('ad', post_ad.get_attribute('href'))


    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()


@pytest.fixture()
def chrome_driver(request):
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    chrome_driver.close()



def test_case02(chrome_driver):
    chrome_driver.get("http://bikroy.com/en/")
    home_page = BikroyHomePage(chrome_driver)
    cities = home_page.get_cities()
    for city in cities.keys():
        print(city)

    for name, link in cities.items():
        # print('visiting {} on link {}'.format(name, link))
        chrome_driver.get(link)
        # Load BikroyCityPage functionality
        city_page = BikroyCityPage(chrome_driver)
        cheapest_product = city_page.get_cheapest_product()
        cheapest_product.click()
        # Load BikroyProductPage functionality
        product_page = BikroyProductPage(chrome_driver)
        posted_on = product_page.get_posted_on()
        assert posted_on is not None

        description = product_page.get_description()
        assert description is not None

        button = product_page.get_seller_mobile_button()
        if not button:
            pytest.skip("No Mobile Number Provided : {}".format(chrome_driver.current_url))
            # self.skipTest("No Mobile Number Provided")
        button.click()
        mobile_number = product_page.get_seller_mobile_number()
        assert mobile_number is not None

        break  # explicitly break after one iteration





def test_case_03(chrome_driver, subtests):
    chrome_driver.get("http://bikroy.com/en/")
    home_page = BikroyHomePage(chrome_driver)
    cities = home_page.get_cities()
    for city in cities.keys():
        print(city)

    for name, link in cities.items():
        with subtests.test(name):
            # print('visiting {} on link {}'.format(name, link))
            chrome_driver.get(link)
            # Load BikroyCityPage functionality
            city_page = BikroyCityPage(chrome_driver)
            cheapest_product = city_page.get_cheapest_product()
            cheapest_product.click()
            # Load BikroyProductPage functionality
            product_page = BikroyProductPage(chrome_driver)

            posted_on = product_page.get_posted_on()
            assert posted_on is not None, "posted_on not provided"

            description = product_page.get_description()
            assert  description is not None, "description not provided"
            # print(chrome_driver.current_url)

            button = product_page.get_seller_mobile_button()
            if not button:
                pytest.skip("No Mobile Number Provided : {}".format(chrome_driver.current_url))
                # self.skipTest("No Mobile Number Provided")
            button.click()
            mobile_number = product_page.get_seller_mobile_number()
            assert mobile_number is not None, "mobile number not provided"


if __name__ == '__main__':
    unittest.main()
