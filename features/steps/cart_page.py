from behave import when, then
from selenium.webdriver.common.by import By

CART = (By.ID, 'nav-cart-count')
PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")


@when('Open cart page')
def open_cart_page(context):
    context.app.header.click_cart()


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    context.app.cart_page.check_cart_item(expected_count)


@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.cart_page.verify_cart_item()


@then('Verify Shopping Cart is empty')
def verify_cart_empty(contex):
    contex.app.cart_page.check_cart_empty()

