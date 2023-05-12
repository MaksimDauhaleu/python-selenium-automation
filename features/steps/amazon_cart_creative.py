from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then("Open an item and add to cart")
def add_to_cart(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href, 'Writing-Computer-Industrial-Folding-Notebook')]").click()
    context.driver.find_element(By.ID, "add-to-cart-button").click()
    context.driver.find_element(By.ID, "attachSiNoCoverage").click()
    sleep(5)


@then("Check if the item is in a cart")
def cart_count_check(context):
    count = context.driver.find_element(By.ID, "nav-cart-count").text
    if count == "1":
        print('Item added')
    else:
        print('Failed')

