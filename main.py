#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import localtime
from requests import post
from json import dumps, load
from os.path import exists, abspath, dirname


def main(event, context):
    with open("/data/cookie.json" if exists("/data/cookie.json") else f"{dirname(abspath(__file__))}/cookie.json", 'r', encoding='utf-8') as f:
        for cookie in load(f):
            print(post(url="http://home.yngqt.org.cn/qndxx/xuexi.ashx", data=dumps({"txtid": localtime()[7] // 7 + 44}), headers={"Cookie": cookie}).text)
            print(post(url="http://home.yngqt.org.cn/qndxx/user/qiandao.ashx", headers={"Cookie": cookie}).text)


if __name__ == '__main__':
    main("", "")

