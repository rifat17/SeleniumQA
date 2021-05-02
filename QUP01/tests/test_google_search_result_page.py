import unittest
import pytest
from selenium import webdriver

from QUP01.src.pages import google_home_page, google_search_result


class GoogleSearchResultPage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.get("http://google.com")
        self.driver.implicitly_wait(10)
    @pytest.mark.skip("problem in doodle xpath")
    def test_check_page_loaded(self):
        drivers = self.driver
        search_kw = "bikroy mobile"

        home_page = google_home_page.GoogleHomePage(drivers)
        home_page.click_a_suggestion(search_kw)

        search_result_page = google_search_result.GoogleSearchResultPage(drivers)

        actual = search_result_page.check_page_loaded()
        expected = True

        self.assertEqual(actual, expected)

    def test_check_search_result_is_not_empty(self):
        drivers = self.driver
        search_kw = "bikroy mobile"

        home_page = google_home_page.GoogleHomePage(drivers)
        home_page.click_a_suggestion(search_kw)

        search_result_page = google_search_result.GoogleSearchResultPage(drivers)

        elements = search_result_page.search_results()
        length = len(elements)

        self.assertGreater(length, 0)

    def test_visit_a_searched_page_randomly(self):
        drivers = self.driver
        search_kw = "bikroy mobile"

        home_page = google_home_page.GoogleHomePage(drivers)
        home_page.click_a_suggestion(search_kw)

        search_result_page = google_search_result.GoogleSearchResultPage(drivers)

        search_result_page.visit_a_page()

    def test_visited_page_title(self):
        drivers = self.driver
        search_kw = "bikroy mobile"

        home_page = google_home_page.GoogleHomePage(drivers)
        home_page.click_a_suggestion(search_kw)

        search_result_page = google_search_result.GoogleSearchResultPage(drivers)
        search_result_page.visit_a_page()

        expected = "Bikroy.com"
        actual = drivers.title
        self.assertIn(expected, actual)








    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
