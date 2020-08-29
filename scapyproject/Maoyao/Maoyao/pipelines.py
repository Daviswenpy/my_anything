# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import pymongo
from .settings import *


class MaoyaoPipeline:
    def process_item(self, item, spider):

        print(item['name'],item['time'])

        return item

class MaoyanMysqlPipeline(object):
    # 爬虫开始时，只执行1次
    def open_spider(self,spider):
        # 一般用于链接数据库
        self.db = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            charset=CHARSET
        )
        self.cur = self.db.cursor()
        print('I am open_spider')




    def process_item(self, item, spider):
        ins = 'insert into filetb values(%s,%s,%s)'
        L = [
            item['name'],
            item['star'],
            item['time'],
        ]
        self.cur.execute(ins,L)
        self.db.commit()
        # create database if not exists maoyandb charset utf8;
        # create table if not exists filetb();

        return item

    # 爬虫结束时，只执行1次
    def close_spider(self,spider):
        # 一般用于断开数据库
        self.cur.close()
        self.db.close()
        print('I am close_spider')


class MaoyanMongoPipeline(object):
    def process_item(self, item, spider):
        return item
