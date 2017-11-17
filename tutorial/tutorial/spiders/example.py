# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['https://kyoto-hifu-landscape.tumblr.com/archive/2017/10']

    def parse(self, response):
         for quote in response.css("div.post_content"):
         	print quote
