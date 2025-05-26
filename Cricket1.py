from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time 
import pandas as pd
import numpy as np
import csv

# driver = webdriver.Chrome()

# driver.get('https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450')


# with open('D:/ICC Mens T20.html','r',encoding='utf8') as f:
#     page = f.read()

# soup = BeautifulSoup(page, features='html.parser')



 
# Path to your saved HTML file
html_file_path = "D:/ICC Mens T20.html"

# Step 1: Load the saved HTML file
with open(html_file_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Step 2: Find the table
table = soup.find("tbody", class_="")

# if table:
#     # Step 3: Extract data
#     rows = table.find_all("tr")
#     print('hello')
#     data = []
#     for row in rows:
#         cells = row.find_all(["th", "td"])  # Include both headers and data cells
#         data.append([cell.get_text(strip=True) for cell in cells])
    
#     # Step 4: Write data to CSV
#     csv_file = "icc_t20_wc_results.csv"
#     with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerows(data)
    
#     print(f"Table data has been successfully saved to {csv_file}.")
# else:
#     print("No table found in the saved HTML file.")


links = []
if table:
    rows = table.find_all("tr")[1:]  # Skip header row
    for row in rows:
        scorecard_cell = row.find_all("td")[-1]  # Assuming the "Scorecard" column is the last column
        if scorecard_cell:
            link_tag = scorecard_cell.find("a")
            if link_tag and link_tag.get("href"):
                links.append(link_tag["href"])
else:
    print("No table found in the saved HTML file.")

# Step 4: Print the links
if links:
    print("Extracted Links from the Scorecard Column:")
    for link in links:
        print(link)
else:
    print("No links found in the Scorecard column.")