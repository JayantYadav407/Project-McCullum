from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get('https://leetcode.com/problemset/')
count = 70
time.sleep(5)
i =1
at_once = list()
while count>0:
    html = driver.page_source
    at_once.append(html)
    try:
        link = driver.find_element(by=By.XPATH,value='//*[@id="__next"]/div[1]/div[4]/div[2]/div[1]/div[4]/div[3]/nav/button[10]').click()
    except Exception as e:
        print(e)
    time.sleep(2)
    i = i+1
    count = count-1
    
print("ho gya")
with open(f'{i}faltu.html','w',encoding='utf-8') as f:
    for i in at_once:
        f.write(i)
print("Done!")