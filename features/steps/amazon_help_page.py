from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PRIVACY_LINK = (By.CSS_SELECTOR, 'a[href="https://www.amazon.com/privacy"]')


@given('Open Amazon T&C page')
def open_tc_page(context):
    context.driver.get\
        ('https://www.amazon.com/gp/help/customer/display.html'
         '/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_org_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_pn_link(context):
    privacy_link = context.driver.find_element(*PRIVACY_LINK)
    context.driver.wait.until\
        (EC.element_to_be_clickable(privacy_link)).click()


@when('Switch to the newly opened window')
def switch_to_new(context):
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_pn_opened(context):
    context.driver.wait.until\
        (EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ'))
    context.driver.find_element\
        (By.XPATH, '//article[@class = "help-content"]//h1[text() = "Amazon.com Privacy Notice"]')


@then('User can close new window and switch back to original')
def to_original_window(context):
    context.driver.switch_to.window(context.original_window)
