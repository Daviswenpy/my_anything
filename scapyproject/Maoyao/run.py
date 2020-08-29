from scrapy import cmdline

cmdline.execute('scrapy crawl maoyan_v2'.split())
# 【1】存入csv文件
# scrapy crawl car - o car.csv
# scrapy crawl car - o car.json
#
# 【2】存入json文件
#
# 【3】注意: settings.py中设置导出编码 - 主要针对json文件
# FEED_EXPORT_ENCODING = 'utf-8'
