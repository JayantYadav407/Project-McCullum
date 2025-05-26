from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import datetime

# Set up Selenium WebDriver (ensure you have a driver installed, e.g., ChromeDriver)
driver = webdriver.Chrome()

# URL of the YouTube playlist
playlist_url = "https://www.youtube.com/playlist?list=PLxCzCOWd7aiEed7SKZBnC6ypFDWYLRvB2"

# Open the playlist in Selenium
driver.get(playlist_url)

# Allow time for page to load fully
time.sleep(5)

# Scroll to the bottom of the page to load all videos (repeat as necessary)
last_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Save the page source to a local file
html_source = driver.page_source
with open("playlist_page.html", "w", encoding="utf-8") as file:
    file.write(html_source)

# Close the browser
driver.quit()

# Parse the saved HTML file with BeautifulSoup
with open("playlist_page.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extract video durations
durations = soup.find_all("span", {"class": "style-scope ytd-thumbnail-overlay-time-status-renderer"})
total_seconds = 0

for duration in durations:
    duration_text = duration.text.strip()  # Example: '12:34'
    time_parts = list(map(int, duration_text.split(":")))
    if len(time_parts) == 2:  # Format: MM:SS
        minutes, seconds = time_parts
        total_seconds += minutes * 60 + seconds
    elif len(time_parts) == 3:  # Format: HH:MM:SS
        hours, minutes, seconds = time_parts
        total_seconds += hours * 3600 + minutes * 60 + seconds

# Convert total seconds to a human-readable format
total_duration = str(datetime.timedelta(seconds=total_seconds))
total_hours = total_seconds / 3600

print(f"Total duration of playlist: {total_duration} (approx. {total_hours:.2f} hours)")
