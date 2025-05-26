import mysql.connector as connector
import pandas as pd
from sqlalchemy import create_engine
import sys

 
# try:
#      connection =connector.connect(
#      host="localhost",
#      username="root",
#      password="DarshanYadav7081",
#      database="wind"
#      )
#      print('database is connected succesfully')
# except:
#     print("Some error occured. Could not connect to database")
# cursor = connection.cursor()
# data.to_sql('Zamoto',connection = engine,index=False,if_exists='replace')
engine = create_engine('mysql+pymysql://root:DarshanYadav7081@localhost:3306/wind')
data = pd.read_csv('Zamato_clean.xls') 

data.to_sql('Zamoto', con=engine, index=False, if_exists='replace')
print('dataset uploaded successfully')
           
  