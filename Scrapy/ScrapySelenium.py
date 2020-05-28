#	* * * * * * * * * * * * * * * * * * * * * * *
#	*					    *
#	*	Scraping quotes with scrapy         *
#	*					    *
#	*              Selenium Scrapy              *
#       *                                           *
#	*		    By	                    *
#	* 					    *
#	*		Fast   Dev                  *
#	*					    *	
#	*			May 28,2020	    *
#	*				            *
#	* * * * * * * * * * * * * * * * * * * * * * *



import scrapy 
from scrapy_selenium import SeleniumRequest

#handling pagination
class Quotes(scrapy.Spider):
	name = 'quotes'
	custom_settings = { 
		'FEED_FORMAT' : 'json',
		'FEED_URI' : 'khi.json'
		# for csv format 
			}
	DOWNLOADER_MIDDLEWARES = {
    		'scrapy_selenium.SeleniumMiddleware': 800
	}
	def start_requests(self):
		urls = [
			'http://quotes.toscrape.com/page/1/',
			'http://quotes.toscrape.com/page/2/',
       		       ]
		for url in urls:
 			yield SeleniumRequest(url=url, callback=self.parse)

	def parse(self, response):
		page = response.url.split("/")[-2]
		# pythonic way
		for quote in response.css('div.quote'):
			yield {
				'quote' : quote.css('span.text::text').get(),
				'author': quote.css('small.author::text').get()
				}	
				
