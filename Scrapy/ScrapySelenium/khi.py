# import packages
import scrapy 
from scrapy_selenium import SeleniumRequest
from shutil import which

# spider class that inherites from scrapy.Spider

class Quotes(scrapy.Spider):

	# name of the spider
	name = 'quote'

	settings = {
            'SELENIUM_DRIVER_NAME': 'chrome',
            'SELENIUM_DRIVER_EXECUTABLE_PATH': which('chromedriver'),
	    'SELENIUM_DRIVER_EXECUTABLE_PATH': '/home/radia/Bureau/scrapy_spider/scrapy_spider/chromedriver',
            'SELENIUM_DRIVER_ARGUMENTS': ['-headless'],
	
        }
			


	# forward downloading
	custom_settings ={
		'FEED_FORMAT' : 'json',
		'FEED_URI' : 'results.json'
	
	}
	DOWNLOADER_MIDDLEWARES = {
    		'scrapy_selenium.SeleniumMiddleware': 800
	}
	
	# function to get start_urls and return a response with SeleniumRequest
	def start_requests(self):
		urls =["http://quotes.toscrape.com/js/"]
		for url in urls : 
			yield SeleniumRequest(url=url , callback = self.parse)

	# parse functions that yields the results
	def parse(self,response):
		 print(response.text)
		
		
