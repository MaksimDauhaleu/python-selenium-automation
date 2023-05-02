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
driver.get('https://www.amazon.com/sign-in')

# find element by Xpath
element_0 = driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
element_1 = driver.find_element(By.ID, "continue")
element_2 = driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").text
element_3 = driver.find_element(By.ID, "auth-fpp-link-bottom")
element_4 = driver.find_element(By.ID, "ap-other-signin-issues-link")
element_5 = driver.find_element(By.ID, "createAccountSubmit")
element_6 = driver.find_element(By.XPATH, "//a[contains(@href, '/ref=ap_signin_notification_condition')]")
element_7 = driver.find_element(By.XPATH, "//a[contains(@href, '/ref=ap_signin_notification_privacy_notice')]")
