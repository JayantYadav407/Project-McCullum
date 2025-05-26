from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()

driver.get('https://www.datacentermap.com/datacenters/')
time.sleep(10)
html = driver.page_source
with open ('DataCenter.html','w',encoding='utf-8') as f:
    f.write(html)

print('Done!')
time.sleep(5)