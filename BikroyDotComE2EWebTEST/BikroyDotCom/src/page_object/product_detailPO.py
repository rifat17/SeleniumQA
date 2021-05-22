from selenium.common.exceptions import NoSuchElementException

from BikroyDotCom.src.locators.product_detail import ProductDetailPageLocator
from BikroyDotCom.src.page_object.base import BasePO


class ProductDetailPO(BasePO):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProductDetailPageLocator

    def get_posted_on_text(self):
        try:
            posted_on = self.driver.find_element(*self.locators.POSTED_ON)
            return posted_on.text
        except:
            return None

    def get_description_text(self):
        description = self.driver.find_element(*self.locators.DESCRIPTION)
        return description.text

    def get_seller_mobile_number_button(self):
        try:
            button = self.driver.find_element(*self.locators.SELLER_MOBILE_BUTTON)
            return button
        except NoSuchElementException:
            return None
            # raise NoSuchElementException('No Mobile Number Provided.')

    def get_seller_mobile_number_text(self):
        try:
            mobile_number = self.driver.find_element(*self.locators.SELLER_MOBILE_NUMBER)
            return mobile_number.text
        except NoSuchElementException:
            return None
            # raise NoSuchElementException('No Mobile Number Provided.')
