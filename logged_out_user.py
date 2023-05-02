from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# Finding Elements
driver.find_element(By.ID, "nav-orders").click()
login_header = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
email_input_field = driver.find_element(By.ID, "ap_email")

# Verifying Elements
assert login_header == "Sign in", "Sign in header is not visible"


if email_input_field.is_displayed():
    print("Email input is present")
else:
    print("Email input isn't present")


