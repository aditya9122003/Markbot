import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

def snpd(strinput):
    PATH="C:\SeleniumDrivers\chromedriver.exe"
    driver=webdriver.Chrome(PATH)
    driver.get("https://www.snapdeal.com")
    search=driver.find_element_by_id('inputValEnter')
    search.send_keys(strinput)
    search.send_keys(Keys.RETURN)
    time.sleep(100000)
    driver.quit()

def snap():
    PATH="C:\SeleniumDrivers\chromedriver.exe"
    driver=webdriver.Chrome(PATH)
    driver.get("https://www.snapdeal.com")
    time.sleep(100000)
    driver.quit()