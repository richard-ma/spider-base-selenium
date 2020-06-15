#!/usr/bin/env python

import spider_base_selenium

class MySpider(spider_base_selenium.Spider):
    def __init__(self):
        self.urls = [
            'http://www.baidu.com',
            'http://www.bing.com',
            'http://www.weibo.com',
        ]

    def parse(self, response):
        print(response.get_response().title)

if __name__ == '__main__':
    my_spider = MySpider()
    engine = spider_base_selenium.Engine()
    engine.run(my_spider)