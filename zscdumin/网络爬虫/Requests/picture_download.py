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


# noinspection PyBroadException
def getImageList(imgList, url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, 'html.parser')
    imgs = soup.find_all('img')
    for img in imgs:
        try:
            href = str(img.attrs['src'])  # 获取照片路径
            if ".jpg" in href:
                imgList.append(href)
        except:
            continue


def printImgList(imgList, fPath):
    i = 1
    for img_url in imgList:
        r = requests.get("http://www.xiaohuar.com" + img_url)
        path = fPath + "img" + str(i) + ".jpg"  # 拼接文件路径
        with open(path, 'wb') as f:  # 写入文件
            f.write(r.content)
            f.close()
            print("文件保存成功")
        i = i + 1


def main():
    imgList = []  # 图片URL列表
    fPath = "F://images//"  # 图片存储路径
    for i in range(2):
        url = "http://www.xiaohuar.com/list-1-" + str(i + 1) + ".html"  # 爬取页面URL
        getImageList(imgList, url)
    printImgList(imgList, fPath)


main()
