# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# * 							    *
# *            Scraping PDF files  			    *
# *							    *
# *               of 248 Guitar licks                       *
# *							    *
# *                    Requests and BeautifulSoup	    *
# *							    *
# *                  BY					    *
# *							    *
# *                       FAST DEV  			    *
# *                                     June 07,2020 	    *
# *							    *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# import packages
import requests
from bs4 import BeautifulSoup

# target url
url = "https://www.dansguitar.com/lick-friday"

# make HTTP request to target url
response = requests.get(url)

# parse the response
html = BeautifulSoup(response.text,'html.parser')

# extract all 'a' tags
urls = html.find_all('a')

# starting
print('**************************Starting*****************************')
# loop over urls to extract pdf urls only 
pdf =[]
	# base url
base_url = 'https://www.dansguitar.com'
for url in urls :
	try :
		# get only pdf urls
		if '.pdf' in url['href']:
			# make get request to download the pdfs
			link = str(base_url+url['href'])
			pdf.append(link)
	
	# exclude all other urls
	except Exception as e:
		print(e)

# count 
i=1
for p in pdf:
	pdfs_url = requests.get(p)
	# write pdf to local file
	filename = str("./Licks/lick%s" %i)
	print(filename)
	with open(filename ,'wb') as f :
		f.write(pdfs_url.content)

	print("Get request done \n")		
	print('file %s has been successfully downloaded \n' %i)		
	i+=1




