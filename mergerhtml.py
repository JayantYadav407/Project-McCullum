html_list = []  # Initialize an empty list to store HTML content
import os   
    # Iterate over all files in the directory


from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
brand_name = list()
detail = list()
price = list()
rating = list()
No_people_rate = list()
for filename in os.listdir('htmlfile'):
    if filename.endswith(".html"):
        filepath = os.path.join('htmlfile', filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
    soup = BeautifulSoup(html,features="html.parser")
    container = soup.find_all('div',{'class':'tUxRFH'})
    # container = list(container)
    # print(len(container))
    for item in container:
        brand_name.append(item.find(class_="KzDlHZ").text)
        price.append(item.find(class_='Nx9bqj _4b5DiR').text)
        rating.append(item.find(class_='XQDdHH').text)
        No_people_rate.append(item.find(class_='_5OesEi').text)
        detail.append(item.find('ul').text)
    

df = pd.DataFrame({
    'brand': brand_name,
    'price': price,
    'rating': rating,
    'No_of_people_rate':No_people_rate,
    'detail': detail,
})

df.to_csv('Flipkart_phone.csv')
print(len(price))


  