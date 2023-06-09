from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

ORDERS_BTN = (By.ID, 'nav-orders')
SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterMoreOnAmazon a')
POPUP_SIGNIN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-signin-button")


@given('Open amazon main page')
def open_amazon(context):
    context.app.main_page.open_main_page()


@when('Click on button from SignIn popup')
def click_sign_in_popup_btn(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(POPUP_SIGNIN_BTN),
        message='Signin btn not clickable'
    ).click()


@when('Search for {search_query}')
def search_amazon(context, search_query):
    context.app.header.search_amazon(search_query)


@when('Click Orders')
def click_orders(context):
    context.app.header.click_orders()


@when('Verify Orders btn present')
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN)


@when('Wait for {sec_amount} sec')
def wait_sec(context, sec_amount):
    sleep(int(sec_amount))


@then('Verify Sign In is clickable')
def verify_signin_popup_btn_clickable(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(POPUP_SIGNIN_BTN),
        message='Signin btn not clickable'
    )


@then('Verify Sign In disappears')
def verify_signin_popup_disappears(context):
    context.driver.wait.until_not(
        EC.visibility_of_element_located(POPUP_SIGNIN_BTN),
        message='Signin btn did not disappear'
    )


@then('Verify there are {expected_amount} links')
def verify_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    print('After conversion: => ', type(expected_amount))

    links_count = len(context.driver.find_elements(*FOOTER_LINKS))  # 36
    print(type(links_count))

    # 36 == 36
    assert links_count == expected_amount, f'Expected {expected_amount} links, but got {links_count}'


@then('Verify Sign In page is opened')
def sign_in_opened(context):
    context.app.base_page.verify_url_contains_query('https://www.amazon.com/ap/signin')


@when('Click on cart icon')
def click_cart(context):
    context.app.header.click_cart()
