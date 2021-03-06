# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class RestaurantSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # url: url of page being crawled
    # title: title of the page
    # date: date that the page is posted
    # content: the crawled content
    url = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
