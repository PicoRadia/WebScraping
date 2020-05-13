import os
import sys

#add vendor directory to module searh path

parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir , 'vendor')
sys.append(vendor_dir)

import requests
import bs4
