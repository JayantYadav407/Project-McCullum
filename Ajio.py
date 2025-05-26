import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
time.sleep(5)
driver.get('https://www.ajio.com/men-backpacks/c/830201001')
old_height = driver.execute_script('return document.body.scrollHeight')
count = 20
while count>0:                                    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

     
    time.sleep(2)
    newHeight = driver.execute_script('return document.body.scrollHeight')
    print(count)
    print(old_height)
    print(newHeight)

    count = count-1
      
time.sleep(5)
html = driver.page_source
with open('ajio.html','w',encoding='utf-8') as f:
    f.write(html)
print(old_height)
