#	* * * * * * * * * * * * * * * * * * * * * * *
#	*					    *
#	*	Scraping quotes with scrapy         *
#	*					    *
#	*              Javascript website           *
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


class QuotesSpider(scrapy.Spider):
	name = "quotes"
	custom_settings = { 
		'FEED_FORMAT' : 'json',
		'FEED_URI' : 'kiko.json'
		# for csv format 
			}
	start_urls= ["http://quotes.toscrape.com/js"]
	def __init__(self):
		scrapy.Spider.__init__(self)
		options = Options()
		options.headless = True
		self.driver = webdriver.Firefox(options=options)
		self.log("Successfully, Started the Selenium Server!")

	def parse(self, response):
		self.logger.info("This url has been identified - " + response.url)
		self.driver.get(response.url)
		response = Selector(text = self.driver.page_source)
		# pythonic way
		divs = response.css('div.quote').getall()	
		for div in divs :
			div = Selector(text=div)
			yield {
				'quote' : div.css('span.text::text').get(),
				'author': div.css('small.author::text').get()
				}

		side_link = response.css('li.next > a::attr("href")').get()
		base_link = 'http://quotes.toscrape.com'
		link = base_link + side_link 
		self.logger.info("next url to be crawled - %s" % link)
		yield scrapy.Request(url=link, callback=self.parse, dont_filter=True)
		}
