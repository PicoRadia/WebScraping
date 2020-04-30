import scrapy
class MySpider(scrapy.Spider):  
    name = "MySpider" 
    def start_requests(self):
            yield scrapy.Request(url = "http://quotes.toscrape.com/",callback = self.parse)
    def parse(self,response):
        quotes = response.css('div.quote span.text::text')
        authors = response.css('div.quote small.author::text')
        for x in response.css('div.quote'):
            yield {
                'author': x.css('small.author::text').get(),
                'quote' : x.css('span.text::text').get()
                 }
        url = "http://quotes.toscrape.com"        
        next_page = response.css("body > div > div:nth-child(2) > div.col-md-8 > nav > ul > li.next > a::attr(href) ").get()
        if next_page is not None :
         url_next_page = url + next_page
        if url_next_page is not None :
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url = url_next_page,callback = self.parse)

    
