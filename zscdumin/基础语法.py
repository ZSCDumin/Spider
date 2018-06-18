#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-25 16:41:09
# @Author  : 杜敏 (2712220318@qq.com)
# @Link    : https://github.com/ZSCDumin
# @Version : $Id$

import os
import re
import requests
from bs4 import BeautifulSoup
from base64 import *
from math import sqrt
import tushare as ts
# k = int(input("enter a number:"))
# if k == 0:
#     print(0)
# elif k == 1:
#     print(1)
# else:
#     print(2)
# list = range(5, 10, 1)  # 前闭后开，最后一个参数表示步长
# list1 = range(5, 5)  # 无输出
# for c in list1:
#     print(c)
# k = sqrt(4)
# def fun(k=True):
#     if k:
#         print("True")
#     else:
#         print("False")
# fun(k=False)
# s='dumin'
# print(s.encode('utf-8'))
# lf = [('AXP', 'American Express Company', '86.40'),('BA', 'The Boeing Company', '122.64')]
# print(lf)
# aDict = {}
# for data in lf:
#     aDict[data[0]] = data[2]
# print(aDict)

# ts.get_h_data('600848',start='2017-03-01',end='2017-03-08')
# r=requests.get("https://www.baidu.com")
# r.encoding='utf-8'
# print(r.text)

# url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"
# try:
# 	kv={'user-agent':'Mozilla/5.0'}
# 	r=requests.get(url,headers=kv)
# 	r.raise_for_status()
# 	r.encoding=r.apparent_encoding
# 	print(r.text[1:1000])
# except:
# 	print("爬虫失败")

# kv={'wd':'Python'}
# r=requests.get("https://www.baidu.com/s",params=kv)
# print(r.status_code)
# print(r.request.url)
# soup=BeautifulSoup('<p>Data</p>','html.parser')
# print(soup.prettify())
import os
import base64


def getThunderUrl(url):
    return ("thunder://".encode("utf-8") + base64.b64encode(('AA' + url + 'ZZ').encode("utf-8"))).decode("utf-8")


#url = "http://sample.sample/sample.jpg"
url = "ed2k: // |file | %E7 % BB % 9D % E5 % 91 % BD % E5 % BE % 8B % E5 % B8 % 88.Better.Call.Saul.S01E01. % E4 % B8 % AD % E8 % 8B % B1 % E5 % AD % 97 % E5 % B9 % 95.BD - HR.AAC.1024x576.x264.mp4 | 530425499 | f8d6953d9ab0ed82b1f3de6c53c16c2d | h = doo6aros4ksn7vzetxkljh33i5zt555s | /"
os.chdir("D:\\Program Files (x86)\\Thunder Network\\Thunder9\\Program\\")
thunderUrl = getThunderUrl(url)
os.system("Thunder.exe -StartType:DesktopIcon \"%s\"" % thunderUrl)
