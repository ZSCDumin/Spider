# -*- coding: utf-8 -*-
import scrapy


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
