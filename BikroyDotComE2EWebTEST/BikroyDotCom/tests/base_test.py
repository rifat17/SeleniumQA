import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        # options.set_capability("profile.managed_default_content_settings.images", 2)
        # options.add_argument("--start-fullscreen")
        options.add_argument('--disable-gpu')

        chrome_prefs = {}
        options.experimental_options["prefs"] = chrome_prefs
        # disable image to load faster in poor internet connection
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def sleep(self, sec):
        SLEEP_SEC = 2
        time.sleep(SLEEP_SEC if sec is None else sec)

    def tearDown(self):
        self.driver.close()

#
# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(Test_HomePO)
#     unittest.TextTestRunner(verbosity=1).run(suite)
