# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from doubanBook.items import DoubanbookItem

class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/tag/']

    rules = (
        Rule(LinkExtractor(allow=(r'/tag/'),restrict_xpaths='//div[@class="article"]'),follow=True),
        Rule(LinkExtractor(allow=(r'/tag/\?start=\d+&type='),restrict_xpaths='//div[@class="paginator"]'),follow=True),
        Rule(LinkExtractor(allow=(r'/subject/\d+/$'),restrict_xpaths='//ul[@class="subject-list"]'),callback='parse_book')

    )

    def parse_book(self, response):
        item = DoubanbookItem()
        if response.xpath('//div[@id="wrapper"]/h1/span/text()').extract():
            item['bookName'] = response.xpath('//div[@id="wrapper"]/h1/span/text()').extract()[0].strip()
        if response.xpath('//div[@id="info"]/a[1]/text()').extract():
            item['author'] = response.xpath('//div[@id="info"]/a[1]/text()').extract()[0].strip()
        yield item
