import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ..locatos.bikroy_locators import BikroyHomePageLocator

class BikroyHomePage(object):

    def __init__(self, driver:webdriver):
        self.driver = driver
        self.locators = BikroyHomePageLocator

    def check_page_loaded(self):
        return True if self.driver.find_element(*self.locators.NAV_LOGO) else False

    def enter_search_kw(self, search_kw):
        self.driver.find_element(*self.locators.SEARCH_BOX).clear()
        self.driver.find_element(*self.locators.SEARCH_BOX).send_keys(search_kw)

        self.driver.find_element(*self.locators.SEARCH_BUTTON).click()
        time.sleep(3)

    def get_products(self):
        return self.driver.find_elements(*self.locators.PRODUCT_LIST)

    def check_nth_product_from_list(self, n=1):
        products = self.get_products()
        # print(products[n])
        # print(dir(products[n]))
        products[n].click()


    def _scroll(self, position_key):
        element = self.driver.find_element(*self.locators.HTML)
        element.send_keys(position_key)

    def scrool_up(self):
        self._scroll(Keys.HOME)

    def scrool_down(self):
        self._scroll(Keys.END)







