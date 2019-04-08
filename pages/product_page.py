from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)



