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

    def check_cart(self):
        self.index_page.open()
        self.index_page.open_product(self.index_page.product_element)
        self.product_page.check_size()
        self.product_page.add_to_cart()
        self.product_page.wait_cart()
        self.checkout_page.open()
        self.checkout_page.delete_by_one_item(self.checkout_page.quantity_count)
        self.quit()

