import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from QUPS_ASSIGNMENT_01_PY.src.locators.bikroy_product import BikroyProductPageLocator


class BikroyProductPage(object):

    def __init__(self, driver) -> None:
        self.driver = driver
        self.locators = BikroyProductPageLocator

    def get_posted_on(self):
        try:
            posted_on = self.driver.find_element(*self.locators.POSTED_ON)
            return posted_on.text
        except:
            return None

    def get_description(self):
        description = self.driver.find_element(*self.locators.DESCRIPTION)
        return description.text

    def get_seller_mobile_button(self):
        try:
            button = self.driver.find_element(*self.locators.SELLER_MOBILE_BUTTON)
            return button
        except NoSuchElementException:
            return None
            # raise NoSuchElementException('No Mobile Number Provided.')

    def get_seller_mobile_number(self):
        try:
            mobile_number = self.driver.find_element(*self.locators.SELLER_MOBILE_NUMBER)
            return mobile_number.text
        except NoSuchElementException:
            return None
            # raise NoSuchElementException('No Mobile Number Provided.')
