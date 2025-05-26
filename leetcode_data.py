from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

Title = list()
Acceptance = list()
Difficulty = list()

with open ('71faltu.html','r',encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html,features='html.parser')
container = soup.find_all('div',{'class':'odd:bg-layer-1 even:bg-overlay-1 dark:odd:bg-dark-layer-bg dark:even:bg-dark-fill-4'})
i = 1
for item in container:
    try:
        Title.append(item.find(class_="truncate").
        text)
       
    except Exception as e:
         Title.append(np.nan)
    try:
     Acceptance.append(item.find('span').text)
    except Exception as e:
        Acceptance.append(np.nan)
    try:
        Difficulty.append(item.find(class_="text-yellow dark:text-dark-yellow").text)
    except:
         
        try:
            Difficulty.append(item.find(class_="text-pink dark:text-dark-pink").text)
        except:
             try:
                 Difficulty.append(item.find(class_="text-olive dark:text-dark-olive").text)
             except:
                 Difficulty.append(np.nan)

# print(Acceptance)  
df = pd.DataFrame({
    'Title': Title,
    'Acceptance': Acceptance,
    'Difficulty': Difficulty
})
df.to_csv('Leetcode_Problem.csv')



