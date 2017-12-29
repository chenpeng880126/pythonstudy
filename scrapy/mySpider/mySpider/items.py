# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#teacher

class ItcastItem(scrapy.Item):
	name = scrapy.Field()
	level = scrapy.Field()
	info = scrapy.Field()

#news
class NewsItem(scrapy.Item):
	title = scrapy.Field()
	time = scrapy.Field()
	href = scrapy.Field()

class DoubanFilmItem(scrapy.Item):
	name = scrapy.Field()
	rank = scrapy.Field()
	href = scrapy.Field()

