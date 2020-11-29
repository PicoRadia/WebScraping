import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


path = '/home/fastdev/Bureau/fastDev/FastDev-master/Toyota/chromedriver'

path2 ='/home/fastdev/Bureau/fastDev/FastDev-master/Toyota/omdakjcmkglenbhjadbccaookpfjihpa-3.3.3-Crx4Chrome.com.crx'

chrome_options = Options()
chrome_options.add_extension(path2)

driver = webdriver.Chrome(executable_path=path, options=chrome_options)
driver.get("https://www.toyota.com/payment-estimator")



