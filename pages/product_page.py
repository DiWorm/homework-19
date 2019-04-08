from selenium.webdriver.support import select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def check_size(self):
        if self.driver.find_element_by_css_selector("select[name='options[Size]']"):
            select.Select(self.driver.find_element_by_css_selector("select[name='options[Size]']")).select_by_value('Medium')

    @property
    def quantity_count(self):
        qc = self.driver.find_element_by_css_selector(".quantity")
        return qc.text

    def add_to_cart(self):
        self.driver.find_element_by_css_selector("[name='add_cart_product'").click()

    def wait_cart(self):
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.quantity'), "1"))


