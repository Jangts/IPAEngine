import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http.request import Request

from wikiIPA.items import WikiipaItem

class DmozSpider(scrapy.Spider):
	name = "wikiIPA"
	allowed_domains = ["en.wiktionary.org"]
	start_urls = ["https://en.wiktionary.org/wiki",
				"https://en.wiktionary.org/wiki/Index:English/a",
				"https://en.wiktionary.org/wiki/Index:English/b",
				"https://en.wiktionary.org/wiki/Index:English/c",
				"https://en.wiktionary.org/wiki/Index:English/d",
				"https://en.wiktionary.org/wiki/Index:English/e",
				"https://en.wiktionary.org/wiki/Index:English/f",
				"https://en.wiktionary.org/wiki/Index:English/h",
				"https://en.wiktionary.org/wiki/Index:English/i",
				"https://en.wiktionary.org/wiki/Index:English/j",
				"https://en.wiktionary.org/wiki/Index:English/k",
				"https://en.wiktionary.org/wiki/Index:English/l",
				"https://en.wiktionary.org/wiki/Index:English/m",
				"https://en.wiktionary.org/wiki/Index:English/n",
				"https://en.wiktionary.org/wiki/Index:English/o",
				"https://en.wiktionary.org/wiki/Index:English/p",
				"https://en.wiktionary.org/wiki/Index:English/q",
				"https://en.wiktionary.org/wiki/Index:English/r",
				"https://en.wiktionary.org/wiki/Index:English/s",
				"https://en.wiktionary.org/wiki/Index:English/t",
				"https://en.wiktionary.org/wiki/Index:English/v",
				"https://en.wiktionary.org/wiki/Index:English/w",
				"https://en.wiktionary.org/wiki/Index:English/x",
				"https://en.wiktionary.org/wiki/Index:English/y",
				"https://en.wiktionary.org/wiki/Index:English/z"]
# 				"https://en.wiktionary.org/wiki/tinnie"
	
	rules = (
        Rule(LinkExtractor(allow=r'/wiki'), callback='parse', follow=True),
    )
	
	def parse(self, response):
		
		word = response.xpath('//a[contains(@href, "/wiki/\w+")]/@href').extract()
		print word
# 		for englishLetter in englishLetters:
# 			item = WikiipaItem()
# # 			item['main_url'] = response.url
# 			
# # 			print "https://en.wiktionary.org/"+englishLetter
# 			word = response.xpath('//a[contains(@href, "/wiki/")]/@href').extract()
# 			print word
# # 			request = scrapy.Request("https://en.wiktionary.org"+englishLetter,callback=self.parse_letters)
#     		return request
      	
      	def parse_letters(self, response):
      		englishLetter = response.xpath('//a[contains(@href, "/wiki/")]/@href').extract()
      		print englishLetter
      		print self
#       		print response
