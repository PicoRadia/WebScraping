import os
import sys

#add vendor directory to module searh path

parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir , 'vendor')
sys.append(vendor_dir)

import requests
import bs4

''' Fast Dev '''
#https://www.worldometers.info/coronavirus/

from bs4 import BeautifulSoup as bs4
import requests
import os
import time

#collecting the html document
response = requests.get("https://www.worldometers.info/coronavirus/")

#making the soup 
soup = bs(response, "html.parser")
head = soup.select("#main_table_countries_today > thead")
print(head)

**********************************
''' Fast Dev '''
#https://www.worldometers.info/coronavirus/

import os
import sys

#add vendor directory to module searh path

parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir , 'vendor')
sys.path.append(vendor_dir)



from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import xlsxwriter


#getting the html
response = requests.get("https://www.worldometers.info/coronavirus/")
#making the soup 
soup = bs(response.text, "html.parser")
table = soup.find('tbody')
table_rows = table.find_all('tr')


country = []
total_deaths= []
total_cases =[]
for tr in table_rows :
    td = tr.find_all('td')
    row = [i.text for i in td]
    country.append(row[0])
    total_cases.append(row[1])
    total_deaths.append(row[3])
    
    
data = pd.DataFrame({
    "Country" : country,
    "Total cases" : total_cases,
    "Total Deaths" : total_deaths
})

#write to an excel file :
writer = pd.ExcelWriter('khi.xlsx' ,engine='xlsxwriter')
data.to_excel(writer,'sheet1')
writer.save()

print(data)
