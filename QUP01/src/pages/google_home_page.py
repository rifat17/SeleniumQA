import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ..locatos.google_locator import GoogleHomePageLocator

class GoogleHomePage(object):

    def __init__(self, driver:webdriver):
        self.driver = driver
        self.locators = GoogleHomePageLocator

    def check_page_loaded(self):
        return True if self.driver.find_element(*self.locators.LOGO) else False

    def enter_search_kw(self, search_kw):
        self.driver.find_element(*self.locators.SEARCH_BOX).clear()
        self.driver.find_element(*self.locators.SEARCH_BOX).send_keys(search_kw)

    def get_search_suggestion_text(self):
        suggestions = self.driver.find_elements(*self.locators.SUGGESTIONS)
        # print(len(suggestions))
        random_search_term = random.choice(suggestions)
        random_search_text = random_search_term.find_element(*self.locators.SUGGESTION).text
        # print(random_search_text)
        return random_search_text


    def click_a_suggestion(self, search_kw):
        # self.driver.find_element(*self.locators.SEARCH_BOX).clear()
        # self.driver.find_element(*self.locators.SEARCH_BOX).send_keys(search_kw)
        self.enter_search_kw(search_kw)
        self.driver.find_element(*self.locators.SEARCH_BOX).send_keys(Keys.ENTER)

    def _scroll(self, position_key):
        element = self.driver.find_element(*self.locators.HTML)
        element.send_keys(position_key)

    def scrool_up(self):
        self._scroll(Keys.HOME)

    def scrool_down(self):
        self._scroll(Keys.END)







