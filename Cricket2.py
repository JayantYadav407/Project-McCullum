import undetected_chromedriver as uc
html = "D:/NAM vs NED Cricket Scorecard.html"
html_file_path =  html  # Update with the correct path
from bs4 import BeautifulSoup
import csv

# Path to your saved HTML file
html_file_path = html  # Update with the correct path

# Step 1: Load the saved HTML file
with open(html_file_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

def funct(soup):
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
    
    save_to_csv("batting_new1.csv",batting, batting_header)
# # save_to_csv("team2_batting.csv", team1_bowling, batting_header)


# # Save Bowling Data for both teams
    save_to_csv("bowling_new2.csv",bowling, bowling_header)
# save_to_csv("team2_bowling.csv", team2_bowling, bowling_header)

funct(soup)

print("CSV files for both teams' batting and bowling data have been saved.")
