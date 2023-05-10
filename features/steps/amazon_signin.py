from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Find element on the page')
def signin_amazon(context):
    context.driver.find_element(By.ID, "nav-orders").click()
    context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    context.driver.find_element(By.ID, "ap_email")


@then('Verify elements')
def verify_signin_results(context):
    login_header = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    email_input_field = context.driver.find_element(By.ID, "ap_email")
    assert login_header == "Sign in", "Sign in header is not visible"
    email_input_field.is_displayed()
