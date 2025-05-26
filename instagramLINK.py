from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
with open('6faltu1.html','r',encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html,features="html.parser")
container = soup.find_all('tr', class_='jss33 jss35')


weblink = []
linkdine = []
i = 0
print("Suru ho gya")
for item in container:
    a = item.find_all('a', target='_blank')
    try:   
        for link in a:
            try:
             href = link.get('href', '').strip()
             print(href)
             if i==0:
              weblink.append(href)
              i+=1
             else :
                linkdine.append(href)
            except:
             print('error')
    except:
       print('error2')
    print(i)
    i=0


df = pd.DataFrame({
    'Web_Link': weblink,
    'Linkdine': linkdine
})
df.to_csv('Company_Link1.csv')
 
# with open("link.txt",'w',encoding='UTF-8') as f:
#     f.write(str(link))