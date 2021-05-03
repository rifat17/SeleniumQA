import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from QUPS_ASSIGNMENT_01_PY.src.locators.bikroy_home import BikroyHomePageLocator


class BikroyHomePage(object):

    def __init__(self, driver) -> None:
        self.driver = driver
        self.locators = BikroyHomePageLocator
        self.cities = {}

    def _scroll(self, position_key):
        self.driver.find_element(*self.locators.HTML).send_keys(position_key)
        # element = self.driver.find_element(*self.locators.HTML)
        # element.send_keys(position_key)

    def scroll_up(self):
        self._scroll(Keys.HOME)

    def scroll_down(self):
        self._scroll(Keys.END)
        time.sleep(2)

    def find_copyright(self):
        return self.driver.find_element(*self.locators.COPYRIGHT)

    def find_POST_YOUR_AD(self):
        return self.driver.find_element(*self.locators.POST_YOUR_AD_A)
        # return self.driver.find_element(*self.locators.POST_YOUR_AD_SPAN).parent

    def get_cities(self):
        cities = self.driver.find_elements(*self.locators.CITIES)
        for city in cities:
            name = city.text
            link = city.get_attribute('href')
            self.cities[name] = link
        return self.cities