from selenium.webdriver.common.by import By
from pages.base_page import Page


class Cart(Page):
    EMPTY_CART_TITLE = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty')
    CART_COUNT = (By.ID, 'nav-cart-count')
    PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")

    def check_cart_empty(self):
        self.verify_element_text('Your Amazon Cart is empty', *self.EMPTY_CART_TITLE)

    def check_cart_item(self, expected_text):
        self.verify_element_text(expected_text, *self.CART_COUNT)

    def verify_cart_item(self):
        self.verify_partial_text(self.driver.product_name, *self.PRODUCT_NAME)
