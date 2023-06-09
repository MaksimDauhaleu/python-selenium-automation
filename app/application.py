from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.base_page import Page
from pages.cart_page import Cart
from pages.product_page import ProductPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.base_page = Page(self.driver)
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.cart_page = Cart(self.driver)
        self.product_page = ProductPage(self.driver)
