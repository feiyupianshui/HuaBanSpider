# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuabanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #分类，终级页面没有
    category = scrapy.Field()
    #作者/用户名
    author = scrapy.Field()
    #画板
    boardname = scrapy.Field()
    #画板简介
    boardescription = scrapy.Field()
    #图片链接
    img_url= scrapy.Field()