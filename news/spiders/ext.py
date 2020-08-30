# -*- coding: utf-8 -*-
import scrapy
import logging


class ExtSpider(scrapy.Spider):
    name = 'ext'
    allowed_domains = ['edition.cnn.com']
    start_urls = ['https://edition.cnn.com/india/']

    def parse(self, response):
        titlelinks = response.xpath("//div[@class='cd__content']/h3/a | /span[@class='cd__headline-text']")
        for link in titlelinks:
            text = link.xpath(".//text()").get()
            li = link.xpath(".//@href").get()

            yield response.follow(url=li, callback = self.parse_link, meta = {'news_title' : text})

    def parse_link(self, response):
        title = response.request.meta['news_title']
        para = response.xpath("//div[@class='l-container']/div[@class='zn-body__paragraph speakable']")
        for pr in para:
            p = pr.xpath(".//text()").get()

            yield{
                'title' : title,
                'para' : p
                
            }
