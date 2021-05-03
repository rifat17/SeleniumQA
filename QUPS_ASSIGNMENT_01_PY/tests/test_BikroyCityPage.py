import time
import unittest
from selenium import webdriver

from QUPS_ASSIGNMENT_01_PY.src.pages.bikroy_city_page import BikroyCityPage
from QUPS_ASSIGNMENT_01_PY.src.pages.bikroy_product_page import BikroyProductPage


class Test_BikroyCityPage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.get("http://bikroy.com/en/ads/dhaka/")
        self.driver.implicitly_wait(5)

    def test_city_X_cheapest_product_info(self):
        city_home_page = BikroyCityPage(self.driver)
        product = city_home_page.get_cheapest_product()
        product.click()

        product_page = BikroyProductPage(self.driver)

        posted_on = product_page.get_posted_on()
        self.assertIsNotNone(posted_on)

        description = product_page.get_description()
        self.assertIsNotNone(description)

        button_view_mobile_number = product_page.get_seller_mobile_button()
        self.assertIsNotNone(button_view_mobile_number)
        button_view_mobile_number.click()

        mobile_number = product_page.get_seller_mobile_number()
        self.assertIsNotNone(mobile_number)



    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
