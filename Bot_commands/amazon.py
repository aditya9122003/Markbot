import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

def amzn(strinput):
    PATH="C:\SeleniumDrivers\chromedriver.exe"
    driver=webdriver.Chrome(PATH)
    driver.get("https://www.amazon.in")
    search=driver.find_element_by_name('field-keywords')
    search.send_keys(strinput)
    search.send_keys(Keys.RETURN)
    time.sleep(100000)
    driver.quit()