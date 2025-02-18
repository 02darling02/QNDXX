#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import time


def everyWeek(cookie, id):
    """
    每周青年大学习
    :param cookie: 传入 Cookie
    :return: 返回是否成功完成 POST 请求的布尔值
    """
    task = '每周青年大学习\n'
    url = 'http://home.yngqt.org.cn/qndxx/xuexi.ashx'
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X) \
                       AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.4(0x1800042c) NetType/4G Language/zh_CN",
        "Cookie": cookie
    }
    data = {"txtid": id}
    try:
        r = requests.post(url, data=json.dumps(data), headers=headers, proxies={"http": None, "https": None})
        r.encoding = r.apparent_encoding
        if r.ok:
            res = r.json()
            print(res)
            if "成功" in res['message'] or "已学习" in res['message']:
                print(f"{task}{res['message']}")
                return True
            else:
                print(f"{task}{res['message']}")
                return False
        else:
            print(f'{task}POST 完成后发生未知错误，错误信息如下：\n{r.text}')
            return False
    except Exception as e:
        print(f"{task}无法完成 POST 访问，错误信息如下：\n{e}")
        return False


def everyDay(cookie):
    """
    每日签到领积分
    :param cookie: 传入 Cookie
    :return: 返回是否成功完成 POST 请求的布尔值
    """
    task = '每日签到领积分\n'
    url = "http://home.yngqt.org.cn/qndxx/user/qiandao.ashx"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X) \
                       AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.4(0x1800042c) NetType/4G Language/zh_CN",
        "Cookie": cookie
    }
    try:
        r = requests.post(url, headers=headers, proxies={"http": None, "https": None})
        r.encoding = r.apparent_encoding
        if r.ok:
            res = r.json()
            print(res)
            if "成功" in res['message'] or "已签到" in res['message']:
                print(f"{task}{res['message']}")
                return True
            else:
                print(f"{task}{res['message']}")
                return False
        else:
            print(f'{task}POST 完成后发生未知错误，错误信息如下：\n{r.text}')
            return False
    except Exception as e:
        print(f"{task}无法完成 POST 访问，错误信息如下：\n{e}")
        return False


def main(event, context):
    """
    腾讯云函数程序入口
    :param event: 可省略
    :param context: 可省略
    :return: 可省略
    """
    with open('./cookie.json', 'r', encoding='utf-8') as f:
        cookies = json.load(f)
    for cookie in cookies:
        if time.localtime()[6] in [0, 1, 2]:  # 周一、周二、周三各学习一遍
            i = 3
            while i:
                id = time.localtime()[7] // 7 + 44
                result = everyWeek(cookie, id)
                if result:
                    i = 0
                else:
                    print('每周阅读失败，准备重试……')
                    i -= 1
        i = 3
        while i:
            result = everyDay(cookie)
            if result:
                i = 0
            else:
                print('每日签到失败，准备重试……')
                i -= 1


if __name__ == '__main__':
    main("", "")

