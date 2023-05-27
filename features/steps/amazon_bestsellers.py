from selenium.webdriver.common.by import By
from behave import given, when, then


TAB_LINKS = (By.XPATH, "//div[contains(@class, '_p13n-zg-nav-tab-all_style_zg-tabs-li')]")


@given('Open Bestsellers Amazon page')
def open_bestsellers_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify there are {expected_amount} Bestseller links')
def verify_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links_count = len(context.driver.find_elements(*TAB_LINKS))
    assert links_count == expected_amount, f'Expected {expected_amount} links, but got {links_count}'



