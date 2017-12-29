#-*- coding:utf-8 -*-

import scrapy
import sys
from mySpider.items import NewsItem

reload(sys)
sys.setdefaultencoding('utf-8')

class ShuSpider(scrapy.Spider):

	name = "shu"
	#allowed_domains = ["http://www.itcast.cn"]
	start_urls = [
	"http://gs.shu.edu.cn/"
	]

	def parse(self,response):
		items = []
		#filename="shu_gs.html"
		#open(filename, 'wb').write(response.body)
		for site in response.xpath('//div[@class="innewsli"]'):
			for part in site.xpath('ul'):
				for li in part.xpath('li'):
					item = NewsItem()

					title = li.xpath('a/text()').extract()
					href = li.xpath('a/@href').extract()
					time = li.xpath('span/text()').extract()

					item['title'] = title
					item['href'] = href
					item['time'] = time

					items.append(item)
		return items