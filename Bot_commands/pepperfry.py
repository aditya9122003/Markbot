import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

def pepperf(strinput):
    PATH="C:\SeleniumDrivers\chromedriver.exe"
    driver=webdriver.Chrome(PATH)
    driver.get("https://www.pepperfry.com")
    search=driver.find_element_by_name('q')
    search.send_keys(strinput)
    search.send_keys(Keys.RETURN)
    time.sleep(100000)
    driver.quit()

def pepper():
    PATH="C:\SeleniumDrivers\chromedriver.exe"
    driver=webdriver.Chrome(PATH)
    driver.get("https://www.pepperfry.com")
    time.sleep(100000)
    driver.quit()