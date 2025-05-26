import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Save the webpage
def save_webpage():
    url = "https://www.google.com/search?q=weather+Lucknow"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open("weather_lucknow.html", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("Webpage saved as weather_lucknow.html")
    else:
        print(f"Failed to fetch webpage. Status code: {response.status_code}")

# Step 2: Extract temperature data and save to CSV
def extract_and_save_to_csv():
    # Load the saved HTML file
    with open("weather_lucknow.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Extract temperature
    temperature_element = soup.find("span", id="wob_tm")
    temperature = temperature_element.text if temperature_element else "N/A"

    # Write to CSV
    csv_file = "weather_lucknow.csv"
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["City", "Temperature (°C)"])  # Header
        writer.writerow(["Lucknow", temperature])     # Data

    print(f"Temperature data saved to {csv_file}")

# Main function
def main():
    save_webpage()
    extract_and_save_to_csv()

if __name__ == "__main__":
    main()
