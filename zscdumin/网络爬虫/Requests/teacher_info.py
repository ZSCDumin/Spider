#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 20:30:54
# @Author  : 杜敏 (2712220318@qq.com)
# @Link    : https://github.com/ZSCDumin
# @Version : $Id$

import requests
import scrapy
from scrapy.selector import Selector


def get_response(url):
    try:
        response = requests.get(url, timeout=30)
        return response.text
    except:
        return "爬取失败"


def main():
    url = "https://movie.douban.com"
    sel = Selector(get_response(url))
    score = sel.xpath('//*[@id="screening"]/div[2]/ul/li[6]/ul/li[3]/span[2]')
    print(score)


main()
