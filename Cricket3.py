from bs4 import BeautifulSoup
# from Selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import undetected_chromedriver as uc
# import pandas as pd
# import numpy as np
# import time
import csv

path = 'D:/Tom Cooper Profile.html'
#driver = uc.Chrome()

with open(path,'r',encoding='Utf8') as f:
  page =f.read()


soup = BeautifulSoup(page,features='html.parser')

# Find the div with the specified class name
data_div =1

# Extract the text data from the div
headers = []
values = []

if data_div:
    items = soup.find_all("p",class_="ds-text-tight-m ds-font-regular ds-uppercase ds-text-typo-mid3")  # Assuming headers and data are in individual <div> tags
    item2 = soup.find_all("span",class_="ds-text-title-s ds-font-bold ds-text-typo")
    for i in range(0, len(items), 2):  # Assuming alternating headers and values
        print(item2[i].text)
        header = items[i].get_text(strip=True)
        value = item2[i].get_text(strip=True) 
        headers.append(header)
        values.append(value)
else:
    print("No data found with the specified class name.")

# Save the extracted data to a CSV file
csv_file_path = "cricketer_profile_data.csv"  # Output CSV file path
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(headers)  # Write the header row
    writer.writerow(values)   # Write the data row

print(f"Extracted data has been saved to {csv_file_path}")




