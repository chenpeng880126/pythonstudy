#-*- coding:utf-8 -*-

import scrapy
import sys
import urllib
import os
from mySpider.items import DoubanFilmItem

reload(sys)
sys.setdefaultencoding('utf-8')

class DoubanSpider(scrapy.Spider):
	name = "douban"
	allowed_domains = ["movie.douban.com"]
	start_urls = [
	"https://movie.douban.com/top250"
	]

	def parse(self,response):
		#filename="doubanTop250.html"
		#open(filename, 'wb').write(response.body)
		
		for site in response.xpath('//div[@class="item"]'):
			item = DoubanFilmItem()

			filmName = site.xpath('div[@class="pic"]/a/img/@alt').extract()[0].decode('utf-8')
			picSrc = site.xpath('div[@class="pic"]/a/img/@src').extract()[0]
			rank = site.xpath('div[@class="pic"]/em/text()').extract()[0]

			item['name'] = filmName
			item['href'] = picSrc
			item['rank'] = rank
			
			if picSrc:
				file_name = "%s.jpg"%(filmName)
				file_path = os.path.join("../../pics",file_name)
				urllib.urlretrieve(picSrc,file_path)

			# 翻页
		next_page = response.xpath('//span[@class="next"]/a/@href')
		if next_page:
			url = response.urljoin(next_page[0].extract())
			yield scrapy.Request(url, self.parse)  