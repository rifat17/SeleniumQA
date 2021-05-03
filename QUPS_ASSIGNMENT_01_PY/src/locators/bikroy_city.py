from selenium.webdriver.common.by import By


class BikroyCityPageLocator(object):
    HTML = (By.TAG_NAME, 'html')
    PRODUCTS_TAG_LI = (By.CSS_SELECTOR, 'ul.list--3NxGO li')
    PRODUCT_PRICE_REL_PEODUCT = (By.CSS_SELECTOR, 'span')
    PRODUCT_URL = (By.XPATH, '//a[@class="card-link--3ssYv gtm-ad-item"]/@href')
    PRODUCT_TITLE = (By.XPATH, '//div[@class="content--3JNQz"]/h2')

