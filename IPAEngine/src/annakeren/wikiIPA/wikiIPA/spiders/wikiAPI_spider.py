import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http.request import Request

from wikiIPA.items import WikiipaItem

class DmozSpider(scrapy.Spider):
	name = "wikiIPA"
	allowed_domains = ["en.wiktionary.org"]
	start_urls = ["https://en.wiktionary.org/wiki"]
	
	rules = (
        Rule(LinkExtractor(allow=r'/wiki'), callback='parse', follow=True),
    )
	
	def parse(self, response):
		
		englishLetters = response.xpath('//a[contains(@href, "/wiki/Index:English")]/@href').extract()
		for englishLetter in englishLetters:
			item = WikiipaItem()
# 			item['main_url'] = response.url
			
# 			print "https://en.wiktionary.org/"+englishLetter
			
			request = scrapy.Request("https://en.wiktionary.org"+englishLetter,callback=self.parse_letters)
# 			yield item
# 			yield Request(englishLetter, self.parse)
    		return request
      	
      	def parse_letters(self, response):
      		englishLetter = response.xpath('//a[contains(@href, "/wiki/")]/@href').extract()
      		print englishLetter
      		print self
#       		print response
