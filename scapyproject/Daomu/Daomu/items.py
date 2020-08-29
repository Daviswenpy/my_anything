# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 确定pipelines处理需要那些数据
    # 1级页面标题，创建文件夹需要
    title = scrapy.Field()
    # 2级页面标题，创建文件需要
    name = scrapy.Field()
    # 3级页面，小说内容
    content = scrapy.Field()



