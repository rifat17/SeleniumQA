from selenium.webdriver.common.by import By


class BikroyAdsPageLocator(object):
    HTML = (By.TAG_NAME, 'html')
    COPYRIGHT = (By.XPATH, '//div[@class="copy-right-section--3P0dH justify-content-space-between--bjSys align-items-normal--vaTgD flex-wrap-nowrap--3IpfJ flex-direction-row--27fh1 flex--3fKk1"]/div[position()=1]') # Copyright © Saltside Technologies
    MORE_from_BIKROY = (By.XPATH, '//div[@class="sm-col-12--30zDS lg-col-2--UArZb  block--3v-Ow"][1]/ul/li/a')
    HELP_n_SUPPORT = (By.XPATH, '//div[@class="sm-col-12--30zDS lg-col-2--UArZb  block--3v-Ow"][2]/ul/li/a')
    FOLLOW_BIKROY = (By.XPATH, '//div[@class="sm-col-12--30zDS lg-col-2--UArZb  block--3v-Ow"][3]/ul/li/a')
    ABOUT_BIKROY = (By.XPATH, '//div[@class="sm-col-12--30zDS lg-col-2--UArZb  block--3v-Ow"][4]/ul/li/a')

