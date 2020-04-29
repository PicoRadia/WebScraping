#import packages and functions
import scrapy
import csv
import json
# -*- coding: utf-8 -*-
# coding: utf-8

#create the spider class
#one page crawl
class MySpider(scrapy.Spider): #this class inherates from the scrapy class Spider
    name = "MySpider" #this name will be used to refer to the spider
    quote_and_author_dictionary={} #dictionnary that will hold the results
    #start_requests method
    def start_requests(self):
        urls = [
            "http://quotes.toscrape.com/",
        ]
        for url in urls : 
            yield scrapy.Request(url = url,callback = self.parse)


    #parse_method
    def parse(self,response):
        #code to parse
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
        else : pass
           
        #dict = {all_authors[i] : all_quotes[i] for i in range(len(all_authors))}
        #print(dict)

        #Creating a dictionnary

        #dict = {authors[i]  : quotes[i] for i in range(len(authors))}
        #print(dict)

        """importing the data """

       # filename = "data.json"
        #with open(filename , 'w' , encoding="UTF-8") as f : 
            #"""Dump the content of the dictionnary in the file f """
           # json.dump(dict,f,indent=4) """

        
    


        #for i in range(len(quotes)) : 
            #single_quote = quotes[i]
           # single_author = authors[i]
            #fill in the dictionnary
            #self.quote_and_author_dictionary[single_author] = single_quote
       # self.print_dictionnary()
        
            

        #printing the dictionary

    def print_dictionnary(self):
        print(self.quote_and_author_dictionary)


            #Dump into a file
            
            #filename="khi.txt"
            #with open(filename,'a') as f :
                #for x in self.quote_and_author_dictionary : 
                    #f.write(x + " " + self.quote_and_author_dictionary[x] +'\n')
            

            
            #dict = self.quote_and_author_dictionary
            #turn into a csv file
           # Myfile = open("data.csv",'w',encoding="UTF-8")
           # writer = csv.writer(Myfile)
            #for key,value in dict.items():
                #writer.writerow([key,value])
           # Myfile.close"""
            
            #turn into a json file

            #convert to DataFrame
            #Add to a Database
            

        


        

    
