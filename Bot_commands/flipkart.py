import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

def fp(strinput):
    print("hi")
    PATH="C:\SeleniumDrivers\chromedriver.exe"
    driver=webdriver.Chrome(PATH)
    driver.get("https://www.flipkart.com")
    search=driver.find_element_by_name('q')
    search.send_keys(strinput)
    search.send_keys(Keys.RETURN)
    time.sleep(100000)
    driver.quit()