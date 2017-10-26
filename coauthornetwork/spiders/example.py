# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "dblpspider"
    #allowed_domains = ["dblp.uni-trier.de/"]
    start_urls = ['http://dblp.uni-trier.de/pers/hd/b/Basuchowdhuri:Partha']


    def parse(self, response):

    	#parse_content(self, response)
    	coauthor_index_content = response.xpath("//div/a[contains(@href, 'http://dblp.uni-trier.de/pers/hd/')]")
    	
    	coauthor_url_list = [ url.encode("utf-8") for url in coauthor_index_content.xpath("@href").extract() ]

    	for url in coauthor_url_list:
    		print "Sending request to .....", url
    		yield scrapy.Request(response.urljoin(url), callback=self.parse_content)
    	


    def parse_content(self, response):
    	#This takes out the Coauthor index part from the html page and returns a SelectorList
    	#Collect all a tag elements under div whose attribute href contains the said string.
    	coauthor_index_content = response.xpath("//div/a[contains(@href, 'http://dblp.uni-trier.de/pers/hd/')]")
    	#Collect all img elements whose title contains show coauthor community
    	coauthor_communities_content = response.xpath("//img[contains(@title, 'show coauthor community')]")
    	#Iterate over the scrapy.selector.unified.SelectorList type variable coauthor_index_content
    	#.extract() returns a list when called over SelectorList type
    	#.xpath() returns a SelectorList when called on SelectorList
    	#List of coauthor names
        #coauthors_name_list = [ name.encode("utf-8") for name in coauthor_index_content.xpath("text()").extract() ]
        #List of coauthor page urls collected from the current page
        #coauthor_url_list = [ url.encode("utf-8") for url in coauthor_index_content.xpath("@href").extract() ]
        #List of communities which the authors lie in the current page
        #coauthor_communities_list = [ community.encode("utf-8") for community in coauthor_communities_content.xpath("@title").extract() ]
        #List of published articles
        #author_articles_published = [ article.encode("utf-8") for article in response.xpath("//span[contains(@class, 'title')]/text()").extract() ]
        
        yield {
        	"author_name": response.xpath("//span[contains(@class, 'name primary')]/text()").extract()[0].encode('utf-8'),
 			"coauthors_name_list": [ name.encode("utf-8") for name in coauthor_index_content.xpath("text()").extract() ],
 			"coauthor_communities_list": [ community.encode("utf-8") for community in coauthor_communities_content.xpath("@title").extract() ],
 			"author_articles_published": [ article.encode("utf-8") for article in response.xpath("//span[contains(@class, 'title')]/text()").extract() ],
 		}

		#coauthor_index_content = response.xpath("//div/a[contains(@href, 'http://dblp.uni-trier.de/pers/hd/')]")
    	
    	coauthor_url_list = [ url.encode("utf-8") for url in coauthor_index_content.xpath("@href").extract() ]

    	for url in coauthor_url_list:
    		print "Sending request to .....", url
    		yield scrapy.Request(response.urljoin(url), callback=self.parse_content)
 		

