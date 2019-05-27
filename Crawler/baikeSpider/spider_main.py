#!/usr/bin/python
# -*- coding: utf-8 -*-
from baikeSpider import url_manager, html_downloader, html_parser, html_outputer

#创建SpiderMain（）方法


class SpiderMain():
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.outputer = html_outputer.HtmlOutputer()
        self.parser = html_parser.HtmlParser()

    def craw(self, root_url):
        count = 1

        # 添加 url
        self.urls.add_new_url(root_url)

        # 当 urls 存在 url 的时候进入循环，否则不进入
        while self.urls.has_new_url():
            try:
                # 获取新的 url
                new_url = self.urls.get_new_url()

                print('craw %d : %s' % (count, new_url))

                # 下载新的 url 的内容
                html_cont = self.downloader.download(new_url)
                # 解析 url 和 数据
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 将新页面的 url 添加到 url 中
                self.urls.add_new_urls(new_urls)
                # 输入器进行数据的收集
                self.outputer.collect_data(new_data)

                # 数据条数可以自行设置，条目越多花费时间越长
                if count == 100:
                    break
                count += 1

            except:
                print('craw failed.')

        html_outputer.HtmlOutputer()

if __name__ == '__main__':
    # 程序入口的爬虫
    root_url = 'https://baike.baidu.com/item/Python/407313'
    spider = SpiderMain()
    spider.craw(root_url)
