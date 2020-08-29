import scrapy
from  ..items import DaomuItem


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    # 解析1级页面,链接，标题
    def parse(self, response):
        # 基准Xpath
        a_list = response.xpath('//li[contains(@id,"menu-item-20")]/a')
        for a in a_list:
            item = DaomuItem()
            item['title'] = a.xpath('//li[contains(@id,"menu-item-20")]/a/text()').get()
            link = a.xpath('//li[contains(@id,"menu-item-20")]/a/@href').get()
            # print(link)
            # 调度器处理，入队列
            yield scrapy.Request(
                url=link,
                # 不同解析函数直接传递数据
                meta={'item':item},
                callback=self.parse_two_page
            )

    # 解析2级页面 章名+详情页link
    def parse_two_page(self,response):
        item = response.meta['item']
        article_list = response.xpath('//article')
        for article in article_list:
            item = DaomuItem()
            item['name'] = article.xpath('//article/a/text()').get()
            item['two_link'] = article.xpath('//article/a/@href').get()
            # 继续交给调度器入队列
            yield scrapy.Request(
                url=item['two_link'],
                meta={'item':item,'name':item['name']},
                callback=self.parse_three_page
            )

    # 解析三级页面，小说内容
    def parse_three_page(self,response):
        item = response.meta['item']
        item['name'] =response.meta['name']
        # 文本内容，段落
        p_list = response.xpath('//article[@class="article-content"]/p/text()').extract()
        # 拼接段落
        content = '\n'.join((p_list))
        item['content'] = content
        yield item


