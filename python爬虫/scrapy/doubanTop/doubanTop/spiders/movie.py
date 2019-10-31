# -*- coding: utf-8 -*-
import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['duoban.com']
    start_urls = ['http://duoban.com/']

    def parse(self, response):
        pass
