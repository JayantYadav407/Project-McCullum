from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

# Initialize WebDriver
def init_driver():
    
    driver = webdriver.Chrome()
    # time.sleep(120)
    return driver

# Get match links
def get_match_links(driver):
    url = "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=14450;type=tournament"
    driver.get(url)

    # Wait for the table to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'table.engineTable > tbody > tr.data1'))
    )

    # Extract links
    rows = driver.find_elements(By.CSS_SELECTOR, 'table.engineTable > tbody > tr.data1')
    links = []
    for row in rows:
        try:
            match_link = row.find_elements(By.TAG_NAME, 'td')[6].find_element(By.TAG_NAME, 'a').get_attribute('href')
            links.append(match_link)
        except Exception as e:
            print(f"Error extracting link: {e}")
    return links

# Parse match details and bowling summary
def parse_match_details(driver, match_url):
    driver.get(match_url)

    # Wait for the scorecard to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div > table.ds-table'))
    )

    # Extract team names and match info
    team_names = driver.find_elements(By.XPATH, '//span[contains(text()," Innings")]/..')
    team1 = team_names[0].text.replace(" Innings", "")
    team2 = team_names[1].text.replace(" Innings", "")
    match_info = f"{team1} Vs {team2}"

    # Extract bowling summaries
    tables = driver.find_elements(By.CSS_SELECTOR, 'div > table.ds-table')
    bowling_summary = []

    def parse_innings(rows, bowling_team):
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if len(cells) >= 11:
                bowler_name = cells[0].text.strip().replace('\xa0', '')
                overs = cells[1].text.strip()
                maiden = cells[2].text.strip()
                runs = cells[3].text.strip()
                wickets = cells[4].text.strip()
                economy = cells[5].text.strip()
                dots = cells[6].text.strip()
                fours = cells[7].text.strip()
                sixes = cells[8].text.strip()
                wides = cells[9].text.strip()
                no_balls = cells[10].text.strip()

                bowling_summary.append({
                    "match": match_info,
                    "bowlingTeam": bowling_team,
                    "bowlerName": bowler_name,
                    "overs": overs,
                    "maiden": maiden,
                    "runs": runs,
                    "wickets": wickets,
                    "economy": economy,
                    "0s": dots,
                    "4s": fours,
                    "6s": sixes,
                    "wides": wides,
                    "noBalls": no_balls
                })

    if len(tables) > 1:
        first_innings_rows = tables[1].find_elements(By.CSS_SELECTOR, 'tbody > tr')
        parse_innings(first_innings_rows, team2)

    if len(tables) > 3:
        second_innings_rows = tables[3].find_elements(By.CSS_SELECTOR, 'tbody > tr')
        parse_innings(second_innings_rows, team1)

    return bowling_summary

# Main function
def main():
    driver = init_driver()
    try:
        match_links = get_match_links(driver)
        all_bowling_summaries = []
        for link in match_links:
            bowling_summary = parse_match_details(driver, link)
            all_bowling_summaries.extend(bowling_summary)

        # Print the bowling summaries
        for summary in all_bowling_summaries:
            print(summary)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
