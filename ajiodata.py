with open('ajio.html','r',encoding='utf-8') as f:
    html = f.read()
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

soup = BeautifulSoup(html, features="html.parser")
print("this is length 500")
container = soup.find_all('div',{'class':'item rilrtl-products-list__item item'})
container = list(container)
print(len(container))
brand = list()
price = list()
rating = list()
for item in container:
    brand.append(item.find('strong').text)
    price.append(item.find('span').text)
    try:
        rating.append(item.find('p').text)
    except:
        rating.append(np.nan)

df = pd.DataFrame({
    'brand': brand,
    'price': price,
    'rating': rating
})
print(df)
df.to_csv('ajio_Data.csv')