import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class BasePO(object):
    SLEEP_SECS = 2

    def __init__(self, driver):
        self.driver = driver
        self.html_locators = (By.TAG_NAME, 'html')
        self.wait = WebDriverWait(self.driver, 10)

    def _scroll(self, position_key):
        self.driver.find_element(*self.html_locators).send_keys(position_key)

    def scroll_to_top(self):
        self._scroll(Keys.HOME)

    def scroll_to_bottom(self):
        self._scroll(Keys.END)

    def sleep(self, sec):
        time.sleep(BasePO.SLEEP_SECS if not sec else sec)
