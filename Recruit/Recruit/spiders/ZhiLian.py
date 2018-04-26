# -*- coding: utf-8 -*-
import scrapy
from Recruit.items import RecruitItem

class ZhilianSpider(scrapy.Spider):
    name = 'ZhiLian'
    area = '北京'
    professional = 'php'
    #url参数  jl地区 kw职位  sm是否列表显示 sb选择排序方式
    start_urls = [
        "https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%s&kw=%s&sm=0&p=1&isfilter=0&fl=530&isadv=0&sb=1" % (area, professional),
    ]

    def parse(self, response):
        items = response.xpath("//table[@class='newlist']")[1:]
        for item in items:
            data = RecruitItem()
            # .//td[@class='gsmc']/a/text()  路径开头需要加。 代表从当前节点选取 不加将抓取珍格格按照页面匹配
            data['positionname'] = item.xpath(".//td[@class='zwmc']/div/a").xpath("string(.)").extract_first()#.xpath("string(.)") 过滤掉目标文本中的标签
            href = item.xpath(".//td[@class='zwmc']/div/a/@href").extract_first()
            data['company'] = item.xpath(".//td[@class='gsmc']/a/text()").extract_first()
            data['salary'] = item.xpath(".//td[@class='zwyx']/text()").extract_first()
            data['workLocation'] = item.xpath(".//td[@class='gzdd']/text()").extract_first()
            meta = data
            yield scrapy.Request(response.urljoin(href), self.parsedetail, meta=meta)
        next_url = response.xpath('//li[@class="pagesDown-pos"]/a/@href').extract_first()
        if next_url:
            yield scrapy.Request(response.urljoin(next_url), self.parse)



    def parsedetail(self,response):
        data = response.meta
        data['publishTime'] = response.xpath("//div[@class='terminalpage-left']/ul/li[3]/strong/span/text()").extract_first()
        data['education'] = response.xpath("//div[@class='terminalpage-left']/ul/li[6]/strong/text()").extract_first()
        data['requirement'] = response.xpath("//div[@class='tab-inner-cont'][1]").xpath("string(.)").extract_first().replace(' ', '').replace('查看职位地图', '')
        yield data