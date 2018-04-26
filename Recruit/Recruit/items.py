# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RecruitItem(scrapy.Item):
    # 职位名
    positionname = scrapy.Field()
    # 学历
    education = scrapy.Field()
    # 工作地点
    workLocation = scrapy.Field()
    # 发布时间
    publishTime = scrapy.Field()
    #工资
    salary = scrapy.Field()
    #公司名
    company = scrapy.Field()
    #要求
    requirement = scrapy.Field()
