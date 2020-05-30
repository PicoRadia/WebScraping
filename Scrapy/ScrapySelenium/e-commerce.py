#	* * * * * * * * * * * * * * * * * * * * * * *
#	*					    *
#	*	Scraping quotes with scrapy         *
#	*					    *
#	*      e-commerce   Selenium   Spider       *
#       *                                           *
#	*		     By                     *
#	* 					    *
#	*		Fast     Dev                *
#	*					    *	
#	*			 May 30,2020	    *
#	*				            *
#	* * * * * * * * * * * * * * * * * * * * * * *


import scrapy 
from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver.firefox.options import Options
import time


class QuotesSpider(scrapy.Spider):
	name = "quotes"
	custom_settings = { 
		'FEED_FORMAT' : 'json',
		'FEED_URI' : 'product.json'
		# for csv format 
			}
	start_urls= ["https://webscraper.io/test-sites/e-commerce/static/computers/laptops"]
	page_number = 1
	def __init__(self):
		scrapy.Spider.__init__(self)
		#headless
		options = Options()
		options.headless = False
		self.driver = webdriver.Firefox(options=options)		
		self.log("Successfully, Started the Selenium Server!")

	def parse(self,response):
		self.logger.info("This url has been identified - " + response.url)
		self.driver.get(response.url)
		response = Selector(text = self.driver.page_source)
		#crawling
		links = response.css('a.title::attr("href")').getall()
		for link in links :
			if link is not None :
				base_url = 'https://webscraper.io/'
				url = base_url + link
				self.logger.info("next url to be crawled - %s" % url)
				yield scrapy.Request(url = url , callback = self.parse_product)
		
		#pagination
		
		link = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=' 
		if QuotesSpider.page_number < 11 : 
			QuotesSpider.page_number +=1
			url = link +str(QuotesSpider.page_number)
			self.logger.info("next url to be crawled - %s" % link)
			yield scrapy.Request(url=url, callback=self.parse,dont_filter=True)
				
		
	def parse_product(self,response):
		self.driver.get(response.url)
		response = Selector(text = self.driver.page_source)
		title = response.css('div.caption > h4::text').get()
		price = response.css('h4.pull-right-price::text').get()
		description = response.css('div.caption > p.description::text').get()
		yield {
			'title' : title,
			'price' : price,
			'description ' : description,
		}
		

		

	
		
