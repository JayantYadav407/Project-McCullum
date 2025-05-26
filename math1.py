import pandas as pd
import numpy as np

# data= pd.read_csv('Flipkart_phone.csv')
# original = data['detail']
# split_data = [item.split('|') for item in original]

 
# df = pd.DataFrame(split_data, columns=['RAM', 'ROM', 'Expandable','Battery','column1','column2'])
# list = df['']
# df = df.drop('column1', axis=1)
# df = df.drop('column2', axis=1)
# df.to_csv('detail.csv')
data = pd.read_csv('Zamato_clean.xls')
print(data)