from selenium import webdriver
from pages.index_page import IndexPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.index_page = IndexPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

    def quit(self):
        self.driver.quit()


