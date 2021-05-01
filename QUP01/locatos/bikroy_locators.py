from selenium.webdriver.common.by import By
class BikroyHomePageLocator(object):
    NAV_LOGO = (By.XPATH, '//div[@class="logo-container--3W5L5"]/*/div')
    SEARCH_BOX = (By.XPATH, '//div[@class="search-row--WRXiU"]//*/form//input')
    SEARCH_BUTTON = (By.XPATH, '//div[@class="search-row--WRXiU"]//*/form/button')
    PRODUCT_LIST = (By.XPATH, '//div[@class="list-wrapper--t_A02"]/ul[@class="list--3NxGO"]/li')
    HTML = (By.TAG_NAME, 'html')


class BikroyProductViewPageLocator(object):
    NAV_LOGO = (By.XPATH, '//div[@class="logo-container--3W5L5"]/*/div')
    PRODUCT_CONTAINER = (By.XPATH, '//div[@class="details-section--2ggRy"]')
    PRODUCT_TITLE = (By.XPATH, '//div[@class="details-section--2ggRy"]//*/h1')
    PRODUCT_TIME_PLACE = (By.XPATH, '//div[@class="details-section--2ggRy"]//*/span')
    PRODUCT_DETAILS = (By.XPATH, '//div[@class="details-section--2ggRy"]//*/div[@class="section--PpGYD"]/div')
    # PRODUCT_PRICE = (By.XPATH, '//div[@class="details-section--2ggRy"]//*/div[@class="section--PpGYD"]//div[@class="amount--3NTpl"')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.amount--3NTpl')
    PRODUCT_INFO = (By.CSS_SELECTOR, 'div.word-break--2nyVq')
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, 'div.description--1nRbz > p')


    #similar Ads
    ADS_SIMILAR_PRODUCT = (By.CSS_SELECTOR, 'ul.similar-ad-card-wrapper--3JRn4')
    # ADS_SIMILAR_PRODUCT = (By.CSS_SELECTOR, 'ul.similar-ad-card-wrapper--3JRn4 li')
    # ADS_SIMILAR_PRODUCT_INNER_RELATIVE = (By.CSS_SELECTOR, ' span')



    HTML = (By.TAG_NAME, 'html')