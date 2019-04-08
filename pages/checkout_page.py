from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.find_element_by_css_selector("div#cart > a.link").click()

    @property
    def quantity_count(self):
        qc = self.driver.find_element_by_css_selector('input[name=quantity]').get_attribute('value')
        return int(qc)

    def delete_by_one_item(self, quantity):
        for _ in range(quantity):
            #self.wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="order_confirmation-wrapper"]/table/tbody/tr[2]/td[1]'), str(quantity)))
            self.driver.find_element_by_css_selector('input[name=quantity]').clear()
            self.driver.find_element_by_css_selector('input[name=quantity]').send_keys(quantity - 1)
            self.driver.find_element_by_css_selector('[name=update_cart_item]').click()
