import pytest

from BikroyDotCom.src.page_object.adsPO import AdsPO
from BikroyDotCom.src.page_object.homePO import HomePO
from BikroyDotCom.src.page_object.product_detailPO import ProductDetailPO
from BikroyDotCom.tests.base_test import BaseTest


class TestCases(BaseTest):

    def setUp(self):
        super(TestCases, self).setUp()

    def test_case_01(self):
        self.driver.get("http://bikroy.com/en/")
        home_page = HomePO(self.driver)
        home_page.scroll_to_bottom()
        self.sleep(1)

        expected = "Copyright © Saltside Technologies"
        actual = home_page.get_copyright_text()

        self.assertEqual(actual, expected)

        home_page.scroll_to_top()
        self.sleep(1)

        self.assertIsNotNone(home_page.find_post_your_ad_button())

    def test_case_02(self):
        self.driver.get("http://bikroy.com/en/")
        home_page = HomePO(self.driver)

        cities = home_page.get_cities()
        # step_1
        for city in cities:
            print(city)
        # step_2
        self.driver.get("https://bikroy.com/en/ads/dhaka")

        ads_page = AdsPO(self.driver)
        # step_3
        lowest_valued_ad = ads_page.get_cheapest_product()
        # step_4
        lowest_valued_ad.click()

        # step_5
        product_detail_page = ProductDetailPO(self.driver)
        posted_on = product_detail_page.get_posted_on_text()
        assert posted_on is not None

        # step_6
        print(posted_on)

        # step_7
        description = product_detail_page.get_description_text()
        assert description is not None

        # step_8
        button = product_detail_page.get_seller_mobile_number_button()

        if button is None:
            pytest.skip("No mobile number there : {}".format(self.driver.current_url))

        button.click()

        # step_9
        mobile_number = product_detail_page.get_seller_mobile_number_text()
        assert mobile_number is not None

    def test_case_03(self):
        self.driver.get("http://bikroy.com/en/")
        home_page = HomePO(self.driver)

        cities = home_page.get_cities()
        # step_1
        for city in cities:
            print(city)

        for city_name, city_link in cities.items():
            with self.subTest(city_name):
                # step_2
                self.driver.get(city_link)

                ads_page = AdsPO(self.driver)
                # step_3
                lowest_valued_ad = ads_page.get_cheapest_product()
                # step_4
                if lowest_valued_ad is None:
                    pytest.skip("No product found in this page {}", format(self.driver.current_url))
                lowest_valued_ad.click()

                # step_5
                product_detail_page = ProductDetailPO(self.driver)
                posted_on = product_detail_page.get_posted_on_text()
                assert posted_on is not None, "posted_on field is empty"

                # step_6
                print(posted_on)

                # step_7
                description = product_detail_page.get_description_text()
                assert description is not None, "description field is empty"

                # step_8
                button = product_detail_page.get_seller_mobile_number_button()

                if button is None:
                    pytest.skip("No mobile number there : {}".format(self.driver.current_url))

                button.click()

                # step_9
                mobile_number = product_detail_page.get_seller_mobile_number_text()
                assert mobile_number is not None, "Mobile number field is empty"

    def test_case_04(self):
        self.driver.get("http://bikroy.com/en/ads")
        ads_page = AdsPO(self.driver)
        ads_page.scroll_to_bottom()
        self.sleep(1)

        expected = "Copyright © Saltside Technologies"
        actual = ads_page.get_copyright_text()

        self.assertEqual(actual, expected)

        links = ads_page.get_all_links_from_MORE_FROM_BIKROY()
        self._visit_pages(links)

        links = ads_page.get_all_links_from_HELP_AND_SUPPORT()
        self._visit_pages(links)

        links = ads_page.get_all_links_from_FOLLOW_BIKROY()
        self._visit_pages(links)

        links = ads_page.get_all_links_from_ABOUT_BIKROY()
        self._visit_pages(links)

        # links = ads_page.get_all_links_from_MORE_FROM_BIKROY()
        # links.append(ads_page.get_all_links_from_HELP_AND_SUPPORT())
        # links.append(ads_page.get_all_links_from_FOLLOW_BIKROY())
        # links.append(ads_page.get_all_links_from_ABOUT_BIKROY())
        # self._visit_pages(links)

    def _visit_pages(self, links):
        for link in links:
            print("Visiting {}".format(link))
            self.driver.get(link)
