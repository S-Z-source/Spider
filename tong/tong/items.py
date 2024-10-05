# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TongItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field() # 股票名字
    Aprice =scrapy.Field() # 股票价值
    code = scrapy.Field() # 股票代码
    gainum = scrapy.Field() # 股票概念数量
    newprice = scrapy.Field() # 股票最新价
    zhangfu = scrapy.Field() # 股票最新涨跌幅
    concept = scrapy.Field() # 股票概念


