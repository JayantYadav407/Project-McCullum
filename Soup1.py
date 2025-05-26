from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup 
import pandas as pd
import numpy as np
import csv
import time

driver = webdriver.Chrome()
source = driver.get('https://www.google.com/search?q=weatherLucknow')
time.sleep(20)

page = driver.page_source
with open('weatherLucknow - Google Search.html','w',encoding='utf-8' ) as f:
    f.write(page)

with open('weatherLucknow - Google Search.html','r',encoding='utf-8' ) as f:
     page  = f.read()
soup = BeautifulSoup(page,features='html.parser' )

text = soup.find("div",class_='vk_bk TylWce SGNhVe').text
temperature_in_deg = text[0:2]
temperature_in_Ferh = text[2:]
print(temperature_in_deg)
print(temperature_in_Ferh)

csv_file = "weather_lucknow.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
     writer = csv.writer(file)
     writer.writerow(["City", f"Temperature {temperature_in_deg} °C"])  # Header
     writer.writerow(["Lucknow",f"Temperature {temperature_in_Ferh} F"]) 
