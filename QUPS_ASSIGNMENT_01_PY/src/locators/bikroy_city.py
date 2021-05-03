from selenium.webdriver.common.by import By


class BikroyHomePageLocator(object):
    HTML = (By.TAG_NAME, 'html')
    COPYRIGHT = (By.XPATH, '//div[@class="col-8 copyright"]') # Copyright © Saltside Technologies
    POST_YOUR_AD_SPAN = (By.XPATH, '//span[@class="h4 t-bold btn-post"]')
    POST_YOUR_AD_A = (By.CSS_SELECTOR, 'a.ui-btn.is-important.btn-post')
    CITIES = (By.CSS_SELECTOR, 'div.home-group.is-city p ~ ul li a')

