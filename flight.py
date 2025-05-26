import time
import csv
from itertools import combinations
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
# Setup Selenium WebDriver (Ensure you have ChromeDriver installed)
# service = Service("chromedriver")  # Replace with correct path if needed
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run in headless mode (no UI)
driver = webdriver.Chrome()

# List of Indian cities with airports
indian_cities_with_airports = [
     "Visakhapatnam", 
    "Itanagar", "Dibrugarh", "Guwahati", "Jorhat", "Silchar", "Gaya", "Patna", "Chandigarh", 
    "Ambikapur", "Bilaspur", "Jagdalpur", "Raipur", "Diu", "New Delhi", "Dabolim", "Mopa", 
    "Ahmedabad", "Bhavnagar", "Bhuj", "Jamnagar", "Kandla", "Porbandar", "Rajkot", "Surat", 
    "Vadodara", "Hisar", "Kangra", "Kullu", "Shimla", "Jammu", "Srinagar", "Bokaro", "Deoghar", 
    "Jamshedpur", "Ranchi", "Ballari", "Bengaluru", "Bidar", "Hubli", "Kalaburagi", "Mangaluru", 
    "Mysuru", "Shivamogga", "Kannur", "Kochi", "Kozhikode", "Thiruvananthapuram", "Leh", 
    "Agatti Island", "Bhopal", "Gwalior", "Indore", "Jabalpur", "Khajuraho", "Rewa", 
    "Aurangabad", "Gondia", "Jalgaon", "Kolhapur", "Latur", "Mumbai", "Nagpur", "Nanded", 
    "Nashik", "Pune", "Shirdi", "Solapur", "Sindhudurg", "Imphal", "Shillong", "Aizawl", 
    "Dimapur", "Bhubaneswar", "Jharsuguda", "Rourkela", "Puducherry", "Amritsar", "Bathinda", 
    "Ludhiana", "Pathankot", "Ajmer", "Bikaner", "Jaipur", "Jaisalmer", "Jodhpur", "Udaipur", 
    "Gangtok", "Chennai", "Coimbatore", "Madurai", "Salem", "Tiruchirappalli", "Tuticorin", 
    "Agartala", "Agra", "Aligarh", "Ayodhya", "Bareilly", "Ghaziabad", "Gorakhpur", "Kanpur", 
    "Lucknow", "Prayagraj", "Varanasi", "Dehradun", "Pantnagar", "Haldwani", "Bagdogra", 
    "Balurghat", "Cooch Behar", "Durgapur", "Kolkata"
]


# Generate unique city pairs
city_pairs = list(combinations(indian_cities_with_airports, 2))

# Scraping function
def scrape_flights(source, destination):
    url = f"https://www.budgetticket.in/flights/{source.lower()}-{destination.lower()}"
    
    driver.get(url)
    print("searh time taken")
    print(source)
    print(destination)
    try:
        search_button = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[2]/div[2]/div/label[2]/span")  # Replace with correct XPath
        search_button.click()
    except:
        print('done!')
    time.sleep(2)  # Wait for page to load
    i = 2
    while i>0:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll to bottom
        i-=1
        time.sleep(1)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    flights_data = []
    flights = soup.find_all("div", class_="col col-md-12")  # Adjust class based on website's structure
    print('here i am 1')
    
    for flight in flights:
        try:

                # flight_detail = flight_detail.split()[3]
                # print(f' {flight_detail} this is ID of flight ')
            print(f'here i  am the length of list filght = {len(flights)}')
            try:
                flight_detail = flight.find("div",class_="d-flex justify-content-start").text.strip().split("\n")[3]
            except:
                flight_detail = np.nan
                print("not found 0 ")
            try:
                airline = flight.find("p", class_="h6 responsive-bold mb-0 ng-binding").text.strip()
            except:
                airline = np.nan
                print("id not found 1")
            try:
                airline_id = flight.find("p",clss_="mb-0 d-inline d-lg-block ng-binding ng-hide").text.strip()

            except:
                try:
                    airline_id = flight.find("p",clss_="mb-0 d-inline d-lg-block ng-binding").text.strip() 
                except:
                    airline_id = np.nan
                    print("id not found 2")
            try:
                departure_time = flight.find("span", class_="text-mild-dark d-block ng-binding h4").text.strip()
            except:
                departure_time = np.nan
                print("id not found 3")
            try:
                arrival_time = flight.find("span", class_="text-mild-dark d-block valign-wrapper ng-binding h4").text.strip()
            except:
                arrival_time = np.nan
                print("id not found 4")
            try:
                price = flight.find("del", class_="ng-binding").text.strip()
            except:
                price = np.nan
                print("id not found 5")
            try:
                Baggage = flight.find("span", class_="Baggage").text.strip()
            except:
                Baggage = np.nan
                print("id not found 6")
            try:
                date = flight.find("span",class_="hide-on-small-and-down mb-0 d-block ng-binding lbl-xmedium font-weight-normal").text.strip()
            except:
                date = np.nan
                print("id not found 7")
            try:
                stop_over = flight.find("span",class_="onechangecolor font-weight-bold responsive-dblock ng-binding ng-scope").text.strip()
            except:
                stop_over = np.nan
                print("id not find 8")
            try:
                source_code = flight.find("span",class_="h6 font-weight-600 mb-0 text-nowrap text-extra-dark ng-binding").text.strip()
            except:
                source_code = np.nan
                print("id not find 9")
            try:
                destination_code = flight.find("span",class_="h6 font-weight-600 text-extra-dark mb-0 text-nowrap ng-binding").text.strip()
            except:
                destination_code = np.nan
                print(" id not find 10")


            try:
                duration = flight.find("span",class_="responsive-dblock text-extra-dark font-weight-bold ng-binding").text.strip()
            except:
                duration = np.nan
                print("id not find 11")
            flights_data.append([flight_detail,source, destination,source_code,destination_code, airline,airline_id, departure_time, arrival_time,duration,date, price,Baggage,stop_over])

            print(f'{flights_data} here i am over')
        except AttributeError:
            continue  # Skip if any data is missing
    
    return flights_data

# Scrape data for all city pairs
all_flights = []
count = 10
leser = 95
for source, destination in city_pairs:
    print(f"Scraping flights from {source} to {destination}...")
    try:
        flight_details = scrape_flights(source, destination)
        time.sleep(2)
        all_flights.extend(flight_details)
    except:
        print("data not found")
    count-=1
    if count==0:
        df1 = pd.DataFrame(all_flights, columns=["flight_details","source", "destination","source_code","destination_code", "airline","airline_id", "departure_time", "arrival_time","duration","date"," price","Baggage","stop_over"])
        df1.to_csv(f"flights_data{leser}.csv", index=False)
        count = 20
        leser+=1
# Close the browser
driver.quit()

# Save data to CSV
df = pd.DataFrame(all_flights, columns=["flight_details","source", "destination","source_code","destination_code", "airline","airline_id", "departure_time", "arrival_time","duration","date"," price","Baggage","stop_over"])
df.to_csv("flights_data_final.csv", index=False)

print("Scraping completed! Data saved to 'flights_data.csv'.")
