import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from QUPS_ASSIGNMENT_01_PY.src.locators.bikroy_city import BikroyCityPageLocator


class BikroyCityPage(object):

    def __init__(self, driver) -> None:
        self.driver = driver
        self.locators = BikroyCityPageLocator

    def get_cheapest_product(self):
        products = self.driver.find_elements(*self.locators.PRODUCTS_TAG_LI)
        # print(len(products))

        min_price = float('inf')
        min_price_product = None
        for product in products:
            text = product.find_element(*self.locators.PRODUCT_PRICE_REL_PEODUCT).text
            # print(product.find_element_by_xpath('//a[@class="card-link--3ssYv gtm-ad-item"]/@href'))
            # print(text.split(' '))
            try:
                raw_amount = text.split(' ')[1]
                amount = float(''.join(raw_amount.split(',')))
                if amount < min_price:
                    min_price = amount
                    min_price_product = product
            except:
                title = product.find_element(*self.locators.PRODUCT_TITLE).text
                print('price not added', title)
                product.screenshot('errors/{}.png'.format(title))
                pass

        print(min_price)
        return min_price_product

