# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "dblp-spider"
    start_urls = ['http://dblp.uni-trier.de/pers/hd/b/Basuchowdhuri:Partha']

    def parse(self, response):

        coauthor_index_content = response.xpath("//div[@class='person']/a")
        coauthor_communities_content = response.xpath("//img[contains(@title, 'show coauthor community')]")
        yield {
            "author_name": response.xpath("//span[contains(@class, 'name primary')]/text()").extract()[0].encode(
                'utf-8'),
            "coauthors_name_list": [name.encode("utf-8") for name in coauthor_index_content.xpath("text()").extract()],
            "coauthor_communities_list": [community.encode("utf-8") for community in
                                          coauthor_communities_content.xpath("@title").extract()],
            "author_articles_published": [article.encode("utf-8") for article in
                                          response.xpath("//span[contains(@class, 'title')]/text()").extract()],
        }

        coauthor_url_list = [url.encode("utf-8") for url in coauthor_index_content.xpath("@href").extract()]

        for url in coauthor_url_list:
            print "Sending request to .....", url
            yield scrapy.Request(response.urljoin(url), callback=self.parse)
