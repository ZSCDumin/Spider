#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-28 20:30:54
# @Author  : 杜敏 (2712220318@qq.com)
# @Link    : https://github.com/ZSCDumin
# @Version : $Id$

import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败"


def getPaperDatalList(url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find(id='title').string
    author = soup.find(id='author').string
    abstract = soup.find(id='abstract').contents[5].string
    print(abstract)


def savePaperDataAsFile(urlList, fPath, num):
    path = fPath + "\\" + "AAAI" + num + ".txt"
    with open(path, 'w') as f:  # 写入文件
        for url in urlList:
            print(url)
            f.write(url + "\n")
        f.close()
        print("文件保存成功")


def main():

    url = "https://aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16583"  # 爬取页面URL
    getPaperDatalList(url)


main()
