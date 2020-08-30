# -*- coding: utf-8 -*-
import scrapy


class ToiextSpider(scrapy.Spider):
    name = 'toiext'
    allowed_domains = ['timesofindia.indiatimes.com']
    start_urls = ['https://timesofindia.indiatimes.com/india']

    def parse(self, response):
        titlelinks = response.xpath("//span[@class='w_tle']/a")
        for link in titlelinks:
            text = link.xpath(".//text()").get()
            li = link.xpath(".//@href").get()

            yield response.follow(url=li, callback = self.parse_link, meta = {'news_title' : text})

    def parse_link(self, response):
        title = response.request.meta['news_title']
        para = response.xpath("//div[@class='_1_Akb clearfix']")
        for pr in para:
            p = pr.xpath(".//text()").get()

            yield{
                'title' : title,
                'para' : p
                
            }

