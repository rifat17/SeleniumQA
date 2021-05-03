import time

from selenium.webdriver.common.keys import Keys

from QUPS_ASSIGNMENT_01_PY.src.locators.bikroy_ads import BikroyAdsPageLocator


class BikroyAdsPage(object):

    def __init__(self, driver) -> None:
        self.driver = driver
        self.locators = BikroyAdsPageLocator
        self.cities = {}

    def _scroll(self, position_key):
        self.driver.find_element(*self.locators.HTML).send_keys(position_key)
        time.sleep(2)

    def scroll_up(self):
        self._scroll(Keys.HOME)

    def scroll_down(self):
        self._scroll(Keys.END)

    def find_copyright(self):
        return self.driver.find_element(*self.locators.COPYRIGHT)

    def _extract_links(self, webElement):
        links = []
        for link_element in webElement:
            href = link_element.get_attribute('href')
            links.append(href)

        return links

    def find_MORE_from_BIKROY(self):
        more_from_bikroy_a = self.driver.find_elements(*self.locators.MORE_from_BIKROY)
        return self._extract_links(more_from_bikroy_a)

    def find_HELP_n_SUPPORT(self):
        help_n_support = self.driver.find_elements(*self.locators.HELP_n_SUPPORT)
        print(len(help_n_support))
        return self._extract_links(help_n_support)

    def find_FOLLOW_BIKROY(self):
        follow_bikroy = self.driver.find_elements(*self.locators.FOLLOW_BIKROY)
        return self._extract_links(follow_bikroy)

    def find_ABOUT_BIKROY(self):
        about_bikroy = self.driver.find_elements(*self.locators.ABOUT_BIKROY)
        return self._extract_links(about_bikroy)
