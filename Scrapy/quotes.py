#	* * * * * * * * * * * * * * * * * * * * * * *
#	*					    *
#	*	Scraping quotes with scrapy         *
#	*					    *
#	*		    By	                    *
#	* 					    *
#	*		Fast   Dev                  *
#	*					    *	
#	*			May 26,2020	    *
#	*				            *
#	* * * * * * * * * * * * * * * * * * * * * * *

import scrapy
from scrapy.crawler import CrawlerProcess
import json

class QuotesScraper(scrapy.Spider):
	name = 'quotes'
	start_urls = ['https://quotes.toscrape.com']
	
	def parse(self,response) :
		# casual way
		quotes = response.css('span.text::text').getall() # to return a list
		authors = response.css('small.author::text').getall()	
		for index in range(len(authors)) : 
			item = {
						'author' : authors[index],
						'quotes' : quotes[index]	
					}
			#yield item  ::  it's cool lol
			result = json.dumps(item,indent = 2) # to pretty print the response
			#print(result)
			
			
		# pythonic way
		for quote in response.css('div.quote'):
			yield {
				'quote' : quote.css('span.text::text').get(),
				'author': quote.css('small.author::text').get()

			}



#run spider

process = CrawlerProcess()
process.crawl(QuotesScraper)
process.start()
