from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Find cart button on the page')
def amazon_cart(context):
    context.driver.find_element(By.ID, "nav-cart").click()


@then('Verify cart is empty')
def verify_amazon_cart(context):
    context.driver.find_element(By.XPATH, "//div[@class = 'a-row sc-your-amazon-cart-is-empty']")

