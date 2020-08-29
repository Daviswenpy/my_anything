import scrapy
from ..items import MaoyaoItem
# 导入items.py
# v2.0 多线程


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan_v2'
    allowed_domains = ['maoyan.com']
    # offset = 0

    # 重写start_requests方法
    def start_requests(self):
        # 所有地址给调度器
        for offset in range(0,91,10):
            url = 'https://maoyan.com/board/4?offset={}'.format(offset)
            # 交给调度器入队列
            yield scrapy.Request(
                url=url,
                callback=self.parse_html,
            )

    def parse_html(self, response):
        # 创建item对象
        item = MaoyaoItem() # scrapy1.5后用字典方式赋值变量
        dd_list = response.xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
        for dd in dd_list:
            # extract() ['乱世佳人']
            # extract_first() 序列化第一个选择器，结果为‘主演’
            #  get() 等同 extract_first()
            item['name']= dd.xpath('./a/@title').extract()[0]
            item['star'] = dd.xpath('.//p[@class="star"]/text()').extract_first()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get() # 1.6 后 与上完全等同

            # 把数据交给管道文件
            yield item




