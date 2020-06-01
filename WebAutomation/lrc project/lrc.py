#	* * * * * * * * * * * * * * * * * * * * * * *
#	*					    *
#	*	Scraping quotes with scrapy         *
#	*					    *
#	*                  LRC gig                  *
#       *                                           *
#	*		     By                     *
#	* 					    *
#	*		Fast     Dev                *
#	*					    *	
#	*			 June 01,2020	    *
#	*				            *
#	* * * * * * * * * * * * * * * * * * * * * * *

# import packages
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys



options = Options()
prefs = {'download.default_directory' : '/home/radia/lrcfiles'}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=options)
# Authentication

url = "https://www.megalobiz.com/auth/login"
driver.get(url)
print('==== \n')
print("Successfully, Started the Selenium Server! \n ")
email = driver.find_element_by_css_selector('#email_macro_1')
email.send_keys('*******@gmail.com')
password = driver.find_element_by_css_selector('#password_macro_1')
password.send_keys('*****')
login = driver.find_element_by_css_selector('#setting_submit_form_macro_2')
login.click()
time.sleep(4)




scroll = 0 # number of page scrolls done
count = 0 # number of files downloaded
# Switch to page 
print('==== \n')
print("Successfully, Switched page! \n ")
url = "https://www.megalobiz.com/lrc/maker/download-music-lyrics-lrc-generated-files?sort=alpha"
driver.get(url)

for i in range(20):
	html = driver.find_element_by_tag_name('html')
	html.send_keys(Keys.END)
	time.sleep(8)
	print(" successfuly scrolled page \n")

print("action \n")
links = driver.find_elements_by_css_selector('span.lyrics_button')
pr =len(links)
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)
time.sleep(8)
print(" successfuly scrolled page \n")

while(pr<10000) :
	links = driver.find_elements_by_css_selector('span.lyrics_button')
	print(len(links))
	for link in links[pr: ]:
		link.click()
		print("button clicked")
		count+=1
	print('==== \n')
	print('%s files downloaded' %count)
		# scroll page		
	html = driver.find_element_by_tag_name('html')
	html.send_keys(Keys.END)
	time.sleep(8)
	print(" successfuly scrolled page \n")
	scroll +=1
	pr = pr+10
