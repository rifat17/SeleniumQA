import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from ..locatos.bikroy_locators import BikroyProductViewPageLocator


class BikroyProductViewPage(object):

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.locators = BikroyProductViewPageLocator

    def check_page_loaded(self):
        return True if self.driver.find_element(*self.locators.NAV_LOGO) else False

    def get_similar_products(self):
        # products = self.driver.find_elements(*self.locators.ADS_SIMILAR_PRODUCT)
        # print(self.driver.page_source)
        # return products
        pass

    def get_cheapest_product_from_ads(self):
        products = self.driver.find_elements(By.CSS_SELECTOR, 'ul.similar-ad-card-wrapper--3JRn4 li')

        min_price = float('inf')
        min_price_product = None
        for product in products:
            text = product.find_element_by_tag_name('span').text
            _, raw_amount = text.split(' ')
            amount = float(''.join(raw_amount.split(',')))
            if amount < min_price:
                min_price = amount
                min_price_product = product

        print(min_price)
        return min_price_product

    def get_cheapest_product_info(self, product=None):
        return self.driver.find_elements(*self.locators.PRODUCT_INFO)