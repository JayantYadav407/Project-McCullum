from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time

with open ('DataCenter.html','r',encoding='utf-8') as f:
 page = f.read()

soup = BeautifulSoup(page,features="html.parser")

right_table = soup.find_all('tr')
country = []
DataCenters = []
if right_table:
        # Extract list items from the right-side table
        right_items = soup.find_all('tr')
        print("\nRight Side Table Items:")
        for item in right_items:
            text1 = item.find_all('td')
            if len(text1)>1:
              country.append(text1[0].text)
              DataCenters.append(text1[1].text)
            # for i in text1:
            #   print(i.text)
            # td_tags = item.find_all('td',class_='right aligned')
            # for td in td_tags:
            #   print(td.text.strip())
else:
    print("Right-side table not found.")
df = pd.DataFrame({
    "Country":country,
    "DataCenters": DataCenters
}
)
df.to_excel('DataCenters.xlsx')
print(DataCenters)
print('Done!')
