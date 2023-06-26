from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select


class Header(Page):
    SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDERS_BTN = (By.ID, 'nav-orders')
    CART_BTN = (By.ID, 'nav-cart')
    DEPARTMENT_BTN = (By.ID, 'searchDropdownBox')

    def search_amazon(self, search_query):
        self.input_text(search_query, *self.SEARCH_FILED)
        self.click(*self.SEARCH_BTN)

    def click_orders(self):
        self.click(*self.ORDERS_BTN)

    def click_cart(self):
        self.click(*self.CART_BTN)

    def changing_dept(self):
        select = Select(self.find_element(*self.DEPARTMENT_BTN))
        select.select_by_value('search-alias=electronics')

