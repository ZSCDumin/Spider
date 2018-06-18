#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 20:30:54
# @Author  : 杜敏 (2712220318@qq.com)
# @Link    : https://github.com/ZSCDumin
# @Version : $Id$

import requests
import json


def getJsonData(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "获取数据失败"


def main():
    # 要翻译的文本
    text = "Artificial intelligence is a branch of computer science."
    # google翻译URL
    url = "http://translate.google.cn/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q=" + text
    data = getJsonData(url)
    JsonData = json.loads(data)
    for item in JsonData[0]:
        print(item[0])


main()
