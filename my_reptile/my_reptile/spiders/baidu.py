# -*- coding: utf-8 -*-
from scrapy import Spider, Request, http
from urllib import parse
import logging
import re
from w3lib.html import remove_tags

logger = logging.getLogger(__name__)


def go_remove_tag(value):
    # 移除标签
    content = remove_tags(value)
    # 移除空格 换行
    return re.sub(r'[\t\r\n\s]', '', content)


class BaiduSpider(Spider):
    name = 'baidu'
    count = 5

    def start_requests(self):
        key_word = '经济指标'
        url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=' + parse.quote(key_word)  # 注意是https
        start_urls = [url]
        yield Request(url, self.parse)

    # dict1 = {'wd': '百度 翻译'}
    # url_data = parse.urlencode(dict1)  # unlencode()将字典{k1:v1,k2:v2}转化为k1=v1&k2=v2

    def parse(self, response):
        logger.debug("-----------------------------------------------------------")
        next_urls = []
        for x in range(self.count):
            next_urls.append(response.xpath(f"//*[@id=\"{x + 1}\"]/h3/a/@href").get())  # 获取到百度关键词的前count条网址
        for u in next_urls:
            logger.debug(u)
            yield Request(url=u, callback=self.get_new_key)
        logger.debug("-----------------------------------------------------------")

    def get_new_key(self, response):
        if response.status is 200:
            logger.debug(response.url)
            print(go_remove_tag(response.body.decode(response.encoding)))
        pass
