from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
SEARCHED_PRODUCTS = (By.CSS_SELECTOR, '[data-component-type= "s-search-result"]')
PRODUCT_IMAGE = (By.CSS_SELECTOR, '[data-component-type= "s-search-result"] div.s-product-image-container')
PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-component-type= "s-search-result"] div.s-title-instructions-style')


@then('Verify search results shown for {expected_result}')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(*RESULT_TEXT).text
    assert expected_result == actual_result,\
        f'Error! Expected {expected_result}' \
        f'but got actual {actual_result}'


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@then('Check for title and image')
def check_products(context):
    exp_products = context.driver.find_elements(*SEARCHED_PRODUCTS)
    expected_products_img = context.driver.find_elements(*PRODUCT_IMAGE)
    expected_products_title = context.driver.find_elements(*PRODUCT_TITLE)

    if len(exp_products) != len(expected_products_img):
        print(f"Products missing {len(exp_products)-len(expected_products_img)} images")

    if len(exp_products) != len(expected_products_title):
        print(f"Products missing {len(exp_products)-len(expected_products_title)} titles")

    assert len(exp_products) == len(expected_products_img) == len(expected_products_title)
