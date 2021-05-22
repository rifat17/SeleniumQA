from selenium.webdriver.support import expected_conditions as EC

from BikroyDotCom.src.locators.home import HomePageLocator
from BikroyDotCom.src.page_object.base import BasePO


class HomePO(BasePO):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocator
        self.cities = None  # store cities in WebElement form

    def get_copyright_text(self):
        self.scroll_to_bottom()
        # self.wait.until(EC.presence_of_element_located(self.locators.COPYRIGHT))
        return self.driver.find_element(*self.locators.COPYRIGHT).text

    def find_post_your_ad_button(self):
        # self.wait.until(EC.presence_of_element_located(self.locators.POST_YOUR_AD_A_TAG))
        return self.driver.find_element(*self.locators.POST_YOUR_AD_A_TAG)

    def get_cities(self):
        if self.cities is None:
            # self.wait.until(EC.presence_of_element_located(self.locators.CITIES))
            self.cities = self.driver.find_elements(*self.locators.CITIES)

        return self._parse_city_from_WebElement()

    def _parse_city_from_WebElement(self):
        cities = {}
        link_attr = 'href'
        for city in self.cities:
            name = city.text
            link = city.get_attribute(link_attr)
            cities[name] = link
        return cities
