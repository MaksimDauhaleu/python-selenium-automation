from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductPage(Page):
    PRODUCT_NAME = (By.ID, 'productTitle')
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')

    def store_product_name(self):
        self.store_name(*self.PRODUCT_NAME)

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

