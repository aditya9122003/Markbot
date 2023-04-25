import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

def amzn_deals():
    PATH="C:\SeleniumDrivers\chromedriver.exe"
    driver=webdriver.Chrome(PATH)
    driver.get("https://www.amazon.in/deals?ref_=nav_cs_gb")
    time.sleep(100000)
    driver.quit()