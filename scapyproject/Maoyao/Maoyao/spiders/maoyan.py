import scrapy
from ..items import MaoyaoItem
# 导入items.py


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4']
    offset = 0

    def parse(self, response):
        # 创建item对象
        item = MaoyaoItem() # scrapy1.5后用字典方式赋值变量
        dd_list = response.xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
        # print(dd_list)
        for dd in dd_list:
            # extract() ['乱世佳人']
            # extract_first() 序列化第一个选择器，结果为‘主演’
            #  get() 等同 extract_first()
            item['name']= dd.xpath('./a/@title').extract()[0]
            item['star'] = dd.xpath('.//p[@class="star"]/text()').extract_first()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get() # 1.6 后 与上完全等同

            # 把数据交给管道文件
            yield item

        # 下一页地址 回调自身，循环，没有多线程
        self.offset += 10
        if self.offset <= 90:
            url = 'https://maoyan.com/board/4?offset={}'.format(self.offset)
            # 把url交给调度器入队列
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )


