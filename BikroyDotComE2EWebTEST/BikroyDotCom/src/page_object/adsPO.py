from selenium.webdriver.support import expected_conditions as EC

from BikroyDotCom.src.locators.ads import AdsPageLocator
from BikroyDotCom.src.page_object.base import BasePO


class AdsPO(BasePO):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AdsPageLocator
        self.products = None

    def _extract_links(self, webElement):
        links = []
        for link_element in webElement:
            href = link_element.get_attribute('href')
            links.append(href)

        return links

    def get_all_links_from_MORE_FROM_BIKROY(self):
        more_from_bikroy_a = self.driver.find_elements(*self.locators.MORE_from_BIKROY)
        return self._extract_links(more_from_bikroy_a)

    def get_all_links_from_HELP_AND_SUPPORT(self):
        help_n_support = self.driver.find_elements(*self.locators.HELP_n_SUPPORT)
        return self._extract_links(help_n_support)

    def get_all_links_from_FOLLOW_BIKROY(self):
        follow_bikroy = self.driver.find_elements(*self.locators.FOLLOW_BIKROY)
        return self._extract_links(follow_bikroy)

    def get_all_links_from_ABOUT_BIKROY(self):
        about_bikroy = self.driver.find_elements(*self.locators.ABOUT_BIKROY)
        return self._extract_links(about_bikroy)

    def get_copyright_text(self):
        # self.scroll_bottom()
        # self.wait.until(EC.presence_of_element_located(self.locators.COPYRIGHT))
        return self.driver.find_element(*self.locators.COPYRIGHT).text

    def get_products(self):
        if self.products is None:
            self.products = self.driver.find_elements(*self.locators.PRODUCTS_TAG_LI)

        return self.products

    def get_cheapest_product(self):
        products = self.get_products()
        # print(len(products))

        min_price = float('inf')
        min_price_product = None
        for product in products:
            text = product.find_element(*self.locators.PRODUCT_PRICE_REL_PEODUCT).text
            try:
                raw_amount = text.split(' ')[1]
                amount = float(''.join(raw_amount.split(',')))
                print("PRICE : ", amount)
                if amount < min_price:
                    min_price = amount
                    min_price_product = product
            except:
                title = product.find_element(*self.locators.PRODUCT_TITLE).text
                print('price not added', title)
                product.screenshot('errors_snapshots/{}.png'.format(title))
                pass

        print("MIN PRICE ", min_price)
        return min_price_product
