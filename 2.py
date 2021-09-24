from selenium import webdriver
import webbrowser
import time
import os,sys

driver = webdriver.Chrome()
driver.get("http://adfoc.us/67575881160061")
time.sleep(9) 
button = driver.find_element_by_xpath('//*[@id="showSkip"]/a/img')
button.click()
time.sleep (3)
driver.quit()
os.system ('3.py')
exit

