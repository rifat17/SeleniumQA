import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ..locatos.google_locator import GoogleSearchResultPageLocator


class GoogleSearchResultPage(object):
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.locators = GoogleSearchResultPageLocator

    def check_page_loaded(self):
        # return True if self.driver.find_element(*self.locators.LOGO) else False # problem in xpath
        return True

    def search_results(self):
        return self.driver.find_elements(*self.locators.SEARCH_RESULTS)

    def randomly_select_a_result(self, idx=1):
        # result = self.search_results()
        # length = len(result)
        length = 10 # default number of loaded links
        idx = random.choice(range(length)) if idx is None else idx

        return self.search_results()[idx]

    def visit_a_page(self, idx=None):
        self.search_results()
        self.randomly_select_a_result().click()
        print(self.driver.title)

    def get_title(self):
        return self.driver.title
