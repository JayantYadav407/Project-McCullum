from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import pandas as pd
import numpy as np
import time
import csv

driver = uc.Chrome()
time.sleep(10)


html_file_path = "D:/ICC Mens T20.html"


def calling(page):
    # Step 2: Find all tables for batting and bowling (assuming 4 tables)
    soup = BeautifulSoup(page,features='html.parser')
    tables = soup.find_all("table", class_="ds-table")
    team1_name = soup.find_all('span',class_="ds-text-tight-l ds-font-bold ds-text-typo hover:ds-text-typo-primary ds-block ds-truncate")
    team1 = team1_name[0].get_text(strip=True)
    team2 = team1_name[1].get_text(strip=True)
    matches_between = f"{team1} Vs {team2}"
    # print(team1_name[0].get_text(strip=True))
    # print(team1_name[1].get_text(strip=True))
    # team2_name = soup.find('span',class_="ds-text-tight-l ds-font-bold ds-text-typo hover:ds-text-typo-primary ds-block ds-truncate")
    # Step 3: Extract Batting Data for Team 1 and Team 2
    def extract_batting_data(table,matches_between,team_name):
        batting_data = []
        rows = table.find_all("tr")
        for row in rows[1:]:  # Skip the header row
            cells = row.find_all("td")
            if len(cells) > 1:  # Exclude rows without data
                # batting_data.append([cell.get_text(strip=True) for cell in cells])            
                row_data = []
                row_data.append(matches_between)
                row_data.append(team_name)
                for cell in cells:
                    row_data.append(cell.get_text(strip=True))
                batting_data.append(row_data)


                
        return batting_data

    # Extract Batting Data for Team 1 (First Table) and Team 2 (Second Table)
    team1_batting = extract_batting_data(tables[0],matches_between,team1)
    team2_batting = extract_batting_data(tables[1],matches_between,team2)

    # Step 4: Extract Bowling Data for Team 1 and Team 2
    def extract_bowling_data(table,matches_between,team_name):
        bowling_data = []
        rows = table.find_all("tr")
        for row in rows[1:]:  # Skip the header row
            cells = row.find_all("td")

            if len(cells) > 1:  # Exclude rows without data
                # bowling_data.append([cell.get_text(strip=True) for cell in cells])
                row_data = []
                row_data.append(matches_between)
                row_data.append(team_name)
                for cell in cells:
                    row_data.append(cell.get_text(strip=True))
                bowling_data.append(row_data)

        return bowling_data

    # Extract Bowling Data for Team 1 (Third Table) and Team 2 (Fourth Table)
    team1_bowling = extract_bowling_data(tables[2],matches_between,team2)
    team2_bowling = extract_bowling_data(tables[3],matches_between,team1)

    # Step 5: Save Batting Data to CSV for both teams
    def save_to_csv(filename, data, header):
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header)  # Write the header
            writer.writerows(data)   # Write the data

    # Batting Headers (Columns)
    batting_header = ["Match","Inningteam","Batsman", "Dismissal", "Runs", "Balls", "4s", "6s", "SR"]
    # Bowling Headers (Columns)
    bowling_header = ["Match","Inningteam","Bowler", "Overs", "Maidens", "Runs", "Wickets", "Economy", "0s", "4s", "6s", "Wides", "No Balls"]

    # Save Batting Data for both teams
    batting = team1_batting+team1_bowling
    bowling = team2_batting+team2_bowling
    print("CSV files for both teams' batting and bowling data have been saved.")
    return batting,bowling

    # save_to_csv("batting.csv",batting, batting_header)
    # # save_to_csv("team2_batting.csv", team1_bowling, batting_header)


    # # Save Bowling Data for both teams
    # save_to_csv("bowling.csv",bowling, bowling_header)
    # save_to_csv("team2_bowling.csv", team2_bowling, bowling_header)







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

batting_header = ["Batsman", "Dismissal", "Runs", "Balls", "4s", "6s", "SR"]
    # Bowling Headers (Columns)
bowling_header = ["Bowler", "Overs", "Maidens", "Runs", "Wickets", "Economy", "0s", "4s", "6s", "Wides", "No Balls"]

batting = []
bowling = []
# Step 4: Print the links
# Step 5: Save Batting Data to CSV for both teams
def save_to_csv(filename, data, header):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write the header
        writer.writerows(data) 
if links:
    print("Extracted Links from the Scorecard Column:")
    count =1
    for link in links:
        l1 = f'{link}'
        driver.get(l1)
        page = driver.page_source
        batting1,bowling1 = calling(page)

        batting+=batting1
        bowling+=bowling1
        time.sleep(5)
        print(link)
        print(batting)
        print(count)
        print()
        count+=1
    save_to_csv("batting_new.csv",batting, batting_header)
    save_to_csv("bowling_new.csv",bowling, bowling_header)
else:
    print("No links found in the Scorecard column.")




