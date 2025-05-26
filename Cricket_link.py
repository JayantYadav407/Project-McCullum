# page_address = "D:/NAM vs NED Cricket Scorecard, 5th Match.html"  # Update this path as needed
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import pandas as pd
import numpy as np
import time
import csv

# Path to your saved HTML file

global counter 
counter = 1
driver = uc.Chrome()
# time.sleep(10)
# Load the saved HTML file
players = set()
def player_details(link_address):
    if link_address in players:
        return
    else:
        players.add(link_address)
    link_address = f'https://www.espncricinfo.com/{link_address}'
    print(link_address)
    print("I am here 3")

    driver.get(link_address)
    time.sleep(5)
    page = driver.page_source

    soup = BeautifulSoup(page,features='html.parser')

# Find the div with the specified class name
    data_div =1

    # Extract the text data from the div
    headers = []
    values = []
   

    if data_div:
        items = soup.find_all("p",class_="ds-text-tight-m ds-font-regular ds-uppercase ds-text-typo-mid3")  # Assuming headers and data are in individual <div> tags
        item2 = soup.find_all("span",class_="ds-text-title-s ds-font-bold ds-text-typo")
        try:
            item3 = soup.find("div",class_="ci-player-bio-content").text
            # print(item3)
            # print("this is detail")
        except:
            print("this is detail error")

        for i in range(0, len(items)):  # Assuming alternating headers and values
            # print(item2[i].text)
            # print(" this is item2")
            header = items[i].get_text(strip=True)
            value = item2[i].get_text(strip=True) 
            headers.append(header)
            values.append(value)
    else:
        print("No data found with the specified class name.")
    headers.append("detail")
    values.append(item3)
    data_dict = {headers[i]: [values[i]] for i in range(len(headers))}

# Create the DataFrame
    data = pd.DataFrame(data_dict)

# Save to CSV
    try:
     print("Attempting to save data...")
    
    # Generate file path
     var = time.time()
     var = str(var)
     csv_file_path = f"D:/temperary/cricketer_profile_data{var}.csv"
     
    
    # Save DataFrame to CSV
     data.to_csv(csv_file_path, index=False)
     print(f"Extracted data has been saved to {csv_file_path}")
    
    # Increment counter
    except Exception as e:
     print(f"An error occurred: {e}")




def Send_link(page_address):
    page_address = f'{page_address}'
    driver.get(page_address)
    time.sleep(2)
    page = driver.page_source
    soup = BeautifulSoup(page,features='html.parser')
    print("I am here")
    # with open(page_address, "r", encoding="utf-8") as file:
    #     soup = BeautifulSoup(file, "html.parser")

    # Find all elements with the specified class name
    target_elements = soup.find_all("div", class_="ds-popper-wrapper ds-inline")

    # Extract all links within these elements
    # print(len(target_elements))
    links = []
    for element in target_elements:
        anchors = element.find_all("a")
        for anchor in anchors:
            href = anchor.get("href")
            if href:
                links.append(href)

    # Print the extracted links
    print("Extracted Links:")
    print(len(links))
    idx = 1
    for link in links:
        print("I am here 2")
        try:
            player_details(link)
        except:
            print("error send_link")
        # print(link)
        # print(idx)
        idx+=1
        print("this is running in under player_datail")
        print(link)




    
    

html_file_path = "D:/ICC Mens T20.html"

# Step 1: Load the saved HTML file
with open(html_file_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Step 2: Find the table
table = soup.find("tbody", class_="")


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
    count = 1
    for link in links:
        try:
         Send_link(link)
        except:
            print("error from link")
        print()
        print(count)
        print()
        print(link)
        count+=1

else:
    print("No links found in the Scorecard column.")

#  line number 135 per path save karna hai
# line number  76 per path save karna hai
# Done!  (*_*)