from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class ProductPage(Page):
    PRODUCT_NAME = (By.ID, 'productTitle')
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    NA_LINK = (By.CSS_SELECTOR, "a[href='/New-Arrivals/b/?_encoding=UTF8&node=17020138011&ref_=sv_sl_6']")
    NA_PANEL = (By.CSS_SELECTOR, ".mm-merch-panel")

    def store_product_name(self):
        self.store_name(*self.PRODUCT_NAME)

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def hover_to_na(self):
        na_element = self.find_element(*self.NA_LINK)
        action = ActionChains(self.driver)
        action.move_to_element(na_element)
        action.perform()
        sleep(5)

    def panel_visible(self):
        self.wait_for_element_appear(*self.NA_PANEL)