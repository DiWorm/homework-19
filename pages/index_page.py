from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class IndexPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://litecart.stqa.ru/en/")
        return self

    def open_product(self, product):
        self.product.click()
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    @property
    def product(self):
        return self.driver.find_element_by_css_selector("div#box-campaigns li.product a.link")

