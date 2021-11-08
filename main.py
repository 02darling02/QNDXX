#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import localtime
from requests import post
from json import dumps, load


def sign(task, cookie):
    url = f"http://home.yngqt.org.cn/qndxx/{task}.ashx"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, "
                      "like Gecko) Mobile/15E148 MicroMessenger/8.0.4(0x1800042c) NetType/4G Language/zh_CN",
        "Cookie": cookie
    }
    res = post(url, data=dumps({"txtid": localtime()[7] // 7 + 44}), headers=headers) if task == "xuexi" else post(url, headers=headers)
    res.encoding = res.apparent_encoding
    print(res.json())


def main(event, context):
    """
    腾讯云函数程序入口
    :param event: 可省略
    :param context: 可省略
    :return: 可省略
    """
    with open('./cookie.json', 'r', encoding='utf-8') as f:
        cookies = load(f)
    for cookie in cookies:
        sign("xuexi", cookie)
        sign("user/qiandao", cookie)


if __name__ == '__main__':
    main("", "")

