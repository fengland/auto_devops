#!/usr/bin/python3
import time, os, logging, pathlib
import requests as rq
from bs4 import BeautifulSoup as bs


class aptos:
    def __init__(self):
        self.URL = 'https://community.aptoslabs.com/it2'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

    def get_343cdc5 (self):
        html = rq.get(self.URL)
        html.encoding = "utf-8"
        soup = bs(html.text, "lxml")

        #print(soup.img['src'])  # 直接输出网站内所有img标签的src链接
        #print(soup.div)
        #print('{}'.format(soup.a.string))  # 输出a标签的内容
        #print(soup.findAll(['tr','td']))
        check_result = soup.find('tbody', class_='before:h-4 before:block font-light').get_text()
        with open(file_name,'a') as f:
            #f.truncate(0)
            f.write(check_result)

        # 输出Top250所有电影的名字
        # name = soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a > span:nth-child(1)')
        # for name in name:
        #     print(name.get_text())


if __name__ == "__main__":
    file_time = time.strftime("%Y%m%d", time.localtime())
    file_dir = pathlib.Path('aptos_check_log')
    if not file_dir.exists():
        file_dir.mkdir()
    file_base_name = "aptos_check" + '.result'
    file_name = file_dir / file_base_name

    cls = aptos()
    cls.get_343cdc5()

