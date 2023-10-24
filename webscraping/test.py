from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# chrome_options = Options()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


login = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
login.send_keys("standard_user")
passwd = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
passwd.send_keys("secret_sauce")
confirm = driver.find_element(By.XPATH, "//input[@type='submit']")
confirm.click()



