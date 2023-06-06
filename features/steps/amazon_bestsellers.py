from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

TAB_LINKS = (By.XPATH, "//div[contains(@class, '_p13n-zg-nav-tab-all_style_zg-tabs-li')]")
BESTSELLER_BTN = (By.XPATH, "//a[contains(@href, 'ref_=nav_cs_bestsellers')]")


@given('Open Bestsellers Amazon page')
def open_bestsellers_amazon(context):
    context.driver.get('https://www.amazon.com')
    context.driver.find_element(*BESTSELLER_BTN).click()
    bestseller_title = context.driver.find_element(By.CSS_SELECTOR, '#zg_banner_text')
    context.driver.wait.until(EC.invisibility_of_element(bestseller_title),
                              context.driver.refresh())


@then('Verify there are {expected_amount} Bestseller links')
def verify_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links_count = len(context.driver.find_elements(*TAB_LINKS))
    assert links_count == expected_amount, f'Expected {expected_amount} links, but got {links_count}'



