from selenium.webdriver.common.by import By


class BikroyProductPageLocator(object):
    HTML = (By.TAG_NAME, 'html')
    POSTED_ON = (By.XPATH, '//span[@class="sub-title--37mkY"]')
    DESCRIPTION = (By.XPATH, '//div[@class="description--1nRbz"]/p')
    # SELLER_MOBILE_BUTTON = (By.XPATH, '//div[@class="display--s3dc8 card--_2NNk"][1]')
    SELLER_MOBILE_BUTTON = (By.XPATH, '//button[@class="contact-section--1qlvP gtm-show-number"]')
    SELLER_MOBILE_NUMBER = (By.XPATH, '//div[@class="phone-numbers--2COKR"]')

