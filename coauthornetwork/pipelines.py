# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class CoauthorNetworkPipeline(object):

    def process_item(self, item, spider):
        if (item["author_name"] is not None or item["author_name"] != ""):
            return item
        else:
            raise DropItem("Missing author name in %s" % item)
