import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv()
username = os.environ.get('username')
password = os.environ.get('password')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = uc.Chrome(options=chrome_options)
driver.get("https://iptorrents.com/login.php")
time.sleep(5)

try:
    signed_in = driver.find_element(By.XPATH, '//form[@action = "/lout.php"]')
except:
    driver.find_element(By.NAME, 'username').send_keys(username)
    time.sleep(2)
    print("typed username")

    driver.find_element(By.NAME, 'password').send_keys(password)
    time.sleep(2)
    print("typed password")

    driver.find_element(By.XPATH, '//input[@value = "Sign In"]').click()
    time.sleep(2)
    print("logged in")

driver.close()
