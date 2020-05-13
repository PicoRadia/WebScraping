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

                    
