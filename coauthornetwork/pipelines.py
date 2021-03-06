# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import pymongo
import read_credential

class CoauthorNetworkPipeline(object):

    collection_name = 'testCollection'

    def __init__(self, mongo_uri, mongo_db):
        self.username, self.pwd, self.url = read_credential.read_credential("/Users/sianand/github/dblp-spider/coauthornetwork/credentials")
        self.mongo_uri = mongo_uri.format(username=self.username, pwd=self.pwd)
        self.mongo_db = mongo_db
        self.db = None
        self.client = None
        self.items = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):

        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        try:
            self.items.append(item)
            if len(self.items) % 10 == 0:
                print "length: ", len(self.items)
                self.db[self.collection_name].insert_many(self.items)
                print "-----------------------BULK INSERT COMPLETE--------------------"
                self.items = []
            else:
                print "False condition"
            return item
        except Exception:
            raise DropItem()

    def close_spider(self, item, spider):
        self.client.close()

