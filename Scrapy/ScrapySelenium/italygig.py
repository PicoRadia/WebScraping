#	* * * * * * * * * * * * * * * * * * * * * * *
#	*					    *
#	*	Scraping quotes with scrapy         *
#	*					    *
#	*      Italy gig    Selenium   Spider       *
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
from tutorial.items import TutorialItem


class Spider(scrapy.Spider):
	name = "italy"
	custom_settings = { 
		'FEED_FORMAT' : 'csv',
		'FEED_URI' : 'part2.csv'
		# for csv format 
			}
	start_urls= ["https://innteckshop.it/index.php?pg=prodotti&mf=TRAS&lim_prodotti=0"]
	page_number = 0
	items = TutorialItem()
	def __init__(self):
		scrapy.Spider.__init__(self)
		#headless
		options = Options()
		options.headless = True
		self.driver = webdriver.Firefox(options=options)		
		self.log("Successfully, Started the Selenium Server!")
		

	def parse(self,response):
		self.logger.info("This url has been identified - " + response.url)
		self.driver.get(response.url)
		response = Selector(text = self.driver.page_source)
		# Crawling
		
		links = response.css('td.prdvb_nome > a::attr("href")').getall()
		for link in links :
			if link is not None :
				base_url = 'https://innteckshop.it/'
				url = base_url + link
				self.logger.info("next url to be crawled - %s" % url)
				yield scrapy.Request(url = url , callback = self.parse_product)
		
		# Pagination [works]
		'''
		link = 'https://innteckshop.it/index.php?pg=prodotti&mf=TRAS&lim_prodotti=' 
		if QuotesSpider.page_number < 300 : 
			QuotesSpider.page_number +=112
			url = link +str(QuotesSpider.page_number)
			self.logger.info("next url to be crawled - %s" % link)
			time.sleep(2)
			yield scrapy.Request(url=url, callback=self.parse,dont_filter=True)
		
		'''

	def parse_product(self,response):
		self.driver.get(response.url)
		response = Selector(text = self.driver.page_source)

		product_code = response.css('td.prdzm_td2 > div::text').get()
		name = response.css('td.prdzm_td2 > h1.prdvb_nome_z::text').get()
		detail = response.css('prdzm_desc >div >p::text').get()
		price = response.css('div.caption > p.description::text').get()
		img = response.css('div.prdzm_img >a.zi >img::attr("src")').get()
		base_url = 'https://innteckshop.it'
		image = base_url + str(img)

		yield {	
			'PRODUCT_CODE' : product_code,
			'NAME' : name,
			'DETTAIL': detail ,
			'IMMAGINE' : image,
			'PRICE ' : price
		}
		

		

	
		
		






