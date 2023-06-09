from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")

    def verify_search_results(self, expected_result):
        self.verify_element_text(expected_result, *self.RESULT_TEXT)

    def click_first_item(self):
        self.click(*self.PRODUCT_PRICE)

