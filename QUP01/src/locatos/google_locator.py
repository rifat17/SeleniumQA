from selenium.webdriver.common.by import By

class GoogleHomePageLocator(object):
    LOGO = (By.XPATH, '//img[@class="lnXdpd"]')
    SEARCH_BOX = (By.XPATH, '//input[@class="gLFyf gsfi"]')
    SUGGESTIONS = (By.XPATH, '//ul[@class="erkvQe"]/li')
    SUGGESTION = (By.XPATH, "./descendant::div[@class='aypzV']/span")
    HTML = (By.TAG_NAME, 'html')

class GoogleSearchResultPageLocator(object):
    # LOGO = (By.XPATH, '//div[@class="logo doodle"]')
    SEARCH_BOX = (By.XPATH, '//input[@class="gLFyf gsfi"]')
    SEARCH_RESULTS = (By.XPATH, '//div[@class="hlcw0c"]/div')
    SEARCH_RESULTS_LINKS = (By.XPATH, '//div[@class="hlcw0c"]/div/*//div[@class="yuRUbf"]/a')
    SEARCH_RESULTS_LINKS_RELATIVE_XPATH = (By.XPATH, './*//div[@class="yuRUbf"]/a')

    HTML = (By.TAG_NAME, 'html')



