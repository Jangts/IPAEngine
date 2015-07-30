import scrapy
class DmozSpider(scrapy.Spider):
	name = "wikiIPA"
	allowed_domains = ["en.wiktionary.org"]
	start_urls = ["https://en.wiktionary.org/wiki/Wiktionary:Main_Page"]
	def parse(self, response):
		filename = response.url.split("/")[-2]
		with open(filename, 'wb') as f:
			f.write(response.body)
