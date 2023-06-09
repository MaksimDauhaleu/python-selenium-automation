from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDERS_BTN = (By.ID, 'nav-orders')
    CART_BTN = (By.ID, 'nav-cart')

    def search_amazon(self, search_query):
        self.input_text(search_query, *self.SEARCH_FILED)
        self.click(*self.SEARCH_BTN)

    def click_orders(self):
        self.click(*self.ORDERS_BTN)

    def click_cart(self):
        self.click(*self.CART_BTN)

