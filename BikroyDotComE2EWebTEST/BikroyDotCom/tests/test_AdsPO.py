from BikroyDotCom.src.page_object.adsPO import AdsPO
from BikroyDotCom.tests.base_test import BaseTest


class Test_AdsPO(BaseTest):

    def setUp(self) -> None:
        super(Test_AdsPO, self).setUp()
        # super().setUp()

        self.driver.get("http://bikroy.com/en/ads/")
        self.page = AdsPO(self.driver)

    def test_find_MORE_FROM_BIKROY_does_not_return_none(self):
        self.assertIsNotNone(self.page.get_all_links_from_MORE_FROM_BIKROY())

    def test_find_HELP_AND_SUPPORT_does_not_return_none(self):
        self.assertIsNotNone(self.page.get_all_links_from_HELP_AND_SUPPORT())

    def test_find_FOLLOW_BIKROY_does_not_return_none(self):
        self.assertIsNotNone(self.page.get_all_links_from_FOLLOW_BIKROY())

    def test_find_ABOUT_BIKROY_does_not_return_none(self):
        self.assertIsNotNone(self.page.get_all_links_from_ABOUT_BIKROY())

    def test_get_cheapest_product_does_not_return_none(self):
        self.assertIsNotNone(self.page.get_cheapest_product())

    def test_get_product_does_not_return_none(self):
        products = self.page.get_products()
        self.assertIsNotNone(products)
        self.assertGreater(len(products), 0)
