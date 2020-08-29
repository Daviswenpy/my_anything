import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        r_list = response.xpath('/html/head/title/text()')
        print('*'*30)
        print(r_list)
        print('*'*30)