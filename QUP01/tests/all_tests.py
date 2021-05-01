import unittest

from HtmlTestRunner import HTMLTestRunner

from QUP01.tests.test_google_home_page import GoogleHomepage
from QUP01.tests.test_google_search_result_page import GoogleSearchResultPage
from QUP01.tests.test_bikroy_home_page import BikroyHomepage
from QUP01.tests.test_bikroy_product_view_page import BikroyProductViewepage

google_home_tests = unittest.TestLoader().loadTestsFromTestCase(GoogleHomepage)
google_search_result_tests = unittest.TestLoader().loadTestsFromTestCase(GoogleSearchResultPage)
bikroy_home_tests = unittest.TestLoader().loadTestsFromTestCase(BikroyHomepage)
bikroy_product_view_tests = unittest.TestLoader().loadTestsFromTestCase(BikroyProductViewepage)

test_suite = unittest.TestSuite([google_home_tests, google_search_result_tests, bikroy_home_tests, bikroy_product_view_tests])

if __name__ == '__main__':
    output = '/home/hasib/PycharmProjects/SeleniumQA/reports'
    runner = HTMLTestRunner(output=output, report_title='QUPS01QA')
    runner.run(test_suite)
