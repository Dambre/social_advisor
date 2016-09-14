# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SynonymsScraperItem(scrapy.Item):
    word = scrapy.Field()
    synonym = scrapy.Field()