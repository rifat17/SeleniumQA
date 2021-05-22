from BikroyDotCom.src.page_object.homePO import HomePO
from BikroyDotCom.tests.base_test import BaseTest


class Test_HomePO(BaseTest):

    def setUp(self) -> None:
        super(Test_HomePO, self).setUp()
        # super().setUp()
        self.driver.get("http://bikroy.com/en/")
        self.home_page = HomePO(self.driver)

    def test_get_copyright_text_is_not_none(self):
        self.assertIsNotNone(self.home_page.get_copyright_text())

    def test_find_post_your_ad_button_is_not_none(self):
        self.assertIsNotNone(self.home_page.find_post_your_ad_button())

    def test_get_cities_is_return_cities(self):
        # print(self.home_page.get_cities())
        self.assertGreater(len(self.home_page.get_cities()), 0)
