import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a GET request to the webpage
url = "https://growjo.com/industry/Analytics/1"
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    exit()

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Locate the table
# Adjust the logic if the table has specific classes or IDs
table = soup.find('table')

if table is None:
    print("No table found on the page.")
    exit()

# Step 4: Extract table headers
headers = [header.text.strip() for header in table.find_all('th')]

# Step 5: Extract table rows
rows = []
for row in table.find_all('tr')[1:]:  # Skip the header row
    cells = row.find_all('td')
    row_data = [cell.text.strip() for cell in cells]
    rows.append(row_data)

# Step 6: Convert data to a Pandas DataFrame
df = pd.DataFrame(rows, columns=headers)

# Step 7: Save the data to an Excel file
output_file = "analytics_companies2.xlsx"
df.to_excel(output_file, index=False)

print(f"Data has been saved to '{output_file}'.")
