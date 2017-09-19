#!/use/bin/env python
#_*_coding:utf-8_*_
import scrapy
import re
from scrapy.http import Request
from bs4 import BeautifulSoup
from scrapy import FromRequest
from ..musqlpipeline.sql import Sql
from huaban.items import HuabanItem

class Myspider(Spider):
    name = 'huaban'
    keyword = '剑三'
    allowed_domain = ['http://huaban.com/']
    start_url = ['pass']

    rules = (
        Rule(LinkExtractor(allow=('')), callback = 'parse_item', follow=True),
    )
    # http: // huaban.com / pins / 1252980069 /
    def parse_item(self,reponse):
        print(response.url)
