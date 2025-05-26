import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver =  webdriver.Chrome()
driver.get("https://www.google.com")
user_input = driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
user_input.send_keys('Campusx')
time.sleep(2)
user_input.send_keys(Keys.ENTER)
time.sleep(20)
link = driver.find_element(by= By.XPATH, value='//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/span/a/h3')
link.click()
time.sleep(20)
link1 = driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/section[2]/a[1]')
link1.click()
time.sleep(20)
