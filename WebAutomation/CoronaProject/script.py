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
import datetime
import schedule
import time


def data_collection():
    #getting the html
    response = requests.get("https://www.worldometers.info/coronavirus/")
    #making the soup 
    soup = bs(response.text, "html.parser")
    table = soup.find('tbody')
    table_rows = table.find_all('tr')

    #data extraction
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

    #cleanind data
    list = [i for i in range(7)]
    data = data.drop(list,axis =0)
    #delete the index column
    data.reset_index()

    current_date = datetime.datetime.now()
    date = str(current_date.strftime("%Y-%m-%d %H:%M"))
    #write to an excel file :
    file_name= date +'.xlsx'
    writer = pd.ExcelWriter(file_name ,engine='xlsxwriter')
    data.to_excel(writer,'sheet1')
    writer.save()
    print("Download done at  : %s \n"%date)

data_collection()
#schedule download every 2 hours
schedule.every(2).hours.do(data_collection)

while True : 
    schedule.run_pending()
    time.sleep(1)
