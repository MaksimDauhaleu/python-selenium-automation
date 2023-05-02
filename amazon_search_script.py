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

driver.find_element(By.ID, "twotabsearchtextbox").send_keys("table")
driver.find_element(By.ID, "nav-search-submit-button").click()


expected_value = '"table"'
actuall_value = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

assert expected_value == actuall_value, f"{expected_value},{actuall_value}"
print('Test passed')


