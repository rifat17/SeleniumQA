from BikroyDotCom.src.page_object.product_detailPO import ProductDetailPO
from BikroyDotCom.src.page_object.adsPO import AdsPO
from BikroyDotCom.tests.base_test import BaseTest


class Test_ProductDetailPO(BaseTest):

    def setUp(self) -> None:
        super(Test_ProductDetailPO, self).setUp()
        # super().setUp()
        product_url = self._get_product_url_from_ads_page("http://bikroy.com/en/ads/")
        self.driver.get(product_url)
        self.page = ProductDetailPO(self.driver)

    def _get_product_url_from_ads_page(self, ads_page_url):
        self.driver.get(ads_page_url)
        ads_page = AdsPO(self.driver)
        product = ads_page.get_products()[0]
        link_attr = 'href'
        url = product.find_element(*ads_page.locators.PRODUCT_URL).get_attribute(link_attr)
        print(url)

        return url

    def test_get_posted_on_text_is_not_none(self):
        self.assertIsNotNone(self.page.get_posted_on_text())

    def test_get_description_text_is_not_none(self):
        self.assertIsNotNone(self.page.get_description_text())

    def test_get_seller_mobile_number_button_is_not_none(self):
        self.assertIsNotNone(self.page.get_seller_mobile_number_button())

    # Before clicking on seller_mobile_number_button
    def test_get_seller_mobile_number_text_is_none(self):
        self.assertIsNotNone(self.page.get_posted_on_text())

    # After clicking on seller_mobile_number_button
    def test_get_seller_mobile_number_text_is_not_none(self):
        self.page.get_seller_mobile_number_button().click()

        self.assertIsNotNone(self.page.get_posted_on_text())
