# -*- coding: utf-8 -*-
import scrapy


class SynonymSpider(scrapy.Spider):
    name = "synonym"
    allowed_domains = ["synonym.com/synonyms/"]
    start_urls = (
        'http://www.synonym.com/synonyms/',
    )

    def parse(self, response):
        pass
