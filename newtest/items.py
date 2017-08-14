# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewtestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DailiIpsItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
    out = scrapy.Field()


class CpItem(scrapy.Item):
    name = scrapy.Field()
    tel = scrapy.Field()
    phone = scrapy.Field()
    linkman = scrapy.Field()
    #cpname = scrapy.Field()
    mail = scrapy.Field()
    make = scrapy.Field()
    address = scrapy.Field()
    linkurl = scrapy.Field()

    info = scrapy.Field()


class AvItem(scrapy.Item):
    title = scrapy.Field()
    pic = scrapy.Field()
    pics = scrapy.Field()
    desc = scrapy.Field()
    avcode = scrapy.Field()
    tags = scrapy.Field()
    url = scrapy.Field()
