# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader.processors import TakeFirst


class VkparseItem(Item):
    id = Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass