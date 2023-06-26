from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.app.product_page.add_to_cart()


@when('Store product name')
def get_product_name(context):
    context.app.product_page.store_product_name()
    # context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    # print(f'Current product: {context.product_name}')


@then('Verify user can click through colors')
def verify_can_click_colors(context):
    actual_colors = []
    expected_colors = ['Black (Baddest Boy)', 'Black (Bandit)', 'Black (Black Sheep)', 'Black (Cock)', 'Black (Freedom)', 'Black (King Lion)', 'Black (Lone Wolf)']
    colors = context.driver.find_elements(*COLOR_OPTIONS) # => [WebElement1, WebElement2, WebElement3]

    for color in colors[:7]:
        # WebElement2
        color.click() # WebElement2.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color]

    assert expected_colors == actual_colors, \
        f'Expected colors {expected_colors} did not match actual {actual_colors}'


@when('Hover over New Arrivals')
def hover_to_na(context):
    context.app.product_page.hover_to_na()


@then('Verify Pop Up is Visible')
def panel_visible(context):
    context.app.product_page.panel_visible()