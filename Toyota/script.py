  
''' Fast Dev '''
# 05/04/2020
# https://www.toyota.com/payment-estimator


from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC


# my functions 

# create function to get header data
def get_headers():
    #model = driver.find_element_by_css_selector('span.DropdownMenu_value__2NjwW').get_text()
    try :
        trim  = driver.find_element_by_class_name('Heading_text__30U6U').get_text()
        print(trim)
    except : 
        print("elem n'existe pas")
   # print(model)
    
    

options = Options()
options.add_argument('log-level=3')

links = []
base_url = "https://www.pes.tms.aws.toyota.com/"

driver = webdriver.Chrome(chrome_options=options)
val = 20 # in seconds
driver.implicitly_wait(val)
href= "https://www.toyota.com/payment-estimator?series=yaris&year=2020&zip=90011"
driver.get(href)

time.sleep(5)
caracter  = input("Enter ok when done")
while(caracter !="ok"):
    time.sleep(5)



print("I'm waiting for further instructions")
print(driver.current_url)

#get_headers()
#driver.find_element_by_class_name("Toggle_button__p77EI").click()
print(driver.find_element_by_css_selector('h1.Heading_text__30U6U'))
# deal with dropdowns

