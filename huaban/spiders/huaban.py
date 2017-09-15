#!/use/bin/env python
#_*_coding:utf-8_*_
import scrapy
from scrapy.spider import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor
from scrapy import FromRequest
from huaban.items import HuabanItem

class myspider(CrawlSpider):
    name = 'huaban'
    keyword = '剑三'
    allowed_domain = ['http://huaban.com/']
    start_url = ['pass']

    def parse_item(self,reponse):
        pass
