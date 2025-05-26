import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
with open('Rocket Launch Schedule.html','r',encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html,features='html.parser')
Model_Name= []
Company = []
Location = []
Rocket_type = []
placed  =[]
Detail = []
Date = []
container = soup.find_all('div',{'class':'cursor-pointer bg-card py-4 px-6 rounded-md border border-card-foreground/20'})
count = 0
for i in container:
    a = i.find('p',class_='text-xl font-semibold').text
    b = i.find('p',class_='font-medium text-foreground/95 hover:underline').text
    try:
        c = i.find('div',class_='px-2 py-1 sm:px-4 sm:py-2 text-foreground/90 text-xs sm:text-sm rounded-lg font-medium bg-[#1D2938] hover:bg-[#303f52]').text
    except:
        c = np.nan
    try:
        d = i.find('div',class_='px-2 py-1 sm:px-4 sm:py-2 text-foreground/90 text-xs sm:text-sm rounded-lg font-medium bg-[#213A3C] hover:bg-[#335155]').text
    except:
        d = np.nan
    try:
        e = i.find('div',class_='px-2 py-1 sm:px-4 sm:py-2 text-foreground/90 text-xs sm:text-sm rounded-lg font-medium bg-[#1E2439]').text
    except:
        e = np.nan
    try:
        f = i.find('p',class_='max-w-[1000px] mt-3 text-sm sm:text-base text-foreground/90').text
    except:
        f = np.nan
    try:
        g = i.find('p',class_='text-foreground/90 text-right text-sm').text
    except:
        g = i.find('p',class_='text-foreground/90 text-right text-sm mt-1').text
    Model_Name.append(a)
    Company.append(b)
    Location.append(c)
    Rocket_type.append(d)
    placed.append(e)
    Detail.append(f)
    Date.append(g)

df = pd.DataFrame({
    'Model_Name':Model_Name,
    'Company': Company,
    'Location':Location,
    'Rocket_type':Rocket_type, 
    'placed': placed,
    'Date': Date,
    'Detail': Detail
})
df.to_excel('Upcoming_rocket_lunches.xlsx')