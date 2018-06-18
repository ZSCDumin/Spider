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


def getUrlList(urlList, downLoadList, url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, 'html.parser')
    urls = soup.find_all('a')
    for url in urls:
        try:
            href = str(url.attrs['href'])  # 获取照片路径
            if "view" in href and "paper" in href and len(href) > 62:
                paperInfoUrl = href.replace("view", "viewPaper")
                print(paperInfoUrl)
                paperDownloadUrl = href.replace("view", "download")
                print(paperDownloadUrl)
                urlList.append(paperInfoUrl)
                downLoadList.append(paperDownloadUrl)
        except:
            continue


def saveUrlAsFile(urlList, downLoadList, fPath, num):
    path = fPath + "\\" + "AAAI_20" + num + "_PaperInfoUrl.txt"
    with open(path, 'w') as f:  # 写入文件
        for url in urlList:
            print(url)
            f.write(url + "\n")
        f.close()
        print("Url列表文件保存成功")

    path = fPath + "\\" + "AAAI_20" + num + "_DownloadUrl.txt"
    with open(path, 'w') as f:  # 写入文件
        for url in downLoadList:
            print(url)
            f.write(url + "\n")
        f.close()
        print("Download列表文件保存成功")


def main():
    urlList = []  # URL列表
    downLoadList = []  # 下载列表

    fPath = "F:\\接单项目\\谷歌翻译\\论文数据\\AAAI"  # 文件存储路径

    for i in range(10, 19):
        num = str(i)
        url = "https://aaai.org/ocs/index.php/AAAI/AAAI" + num + "/schedConf/presentations"  # 爬取页面URL
        print(url)
        getUrlList(urlList, downLoadList, url)
        saveUrlAsFile(urlList, downLoadList, fPath, num)
        urlList.clear()
        downLoadList.clear()


main()
