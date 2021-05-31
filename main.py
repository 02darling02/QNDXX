import requests, json, time


def erverWeek(Cookie): # 每周青年大学习
    url = 'http://home.yngqt.org.cn/qndxx/xuexi.ashx'
    headers = {
        "Host": "home.yngqt.org.cn",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "zh-cn",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://home.yngqt.org.cn",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.4(0x1800042c) NetType/4G Language/zh_CN",
        "Referer": "http://home.yngqt.org.cn/qndxx/",
        "Cookie": Cookie
    }
    data = {
        "txtid": time.localtime()[7] // 7 + 51
    }
    try:
        r = requests.post(url, data=json.dumps(data), headers=headers)
        if r.ok:
            res = r.json()
            if res['code'] == '100' or res['code'] == '102':
                print(res['message'])
            else:
                print(res)
        else:
            print(f'发生未知错误：\n{r.text}')
    except Exception as e:
        print(e)


def everyDay(Cookie): # 每日签到领积分
    url = "http://home.yngqt.org.cn/qndxx/user/qiandao.ashx"
    headers = {
        "Host": "home.yngqt.org.cn",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-cn",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Origin": "http://home.yngqt.org.cn",
        "Content-Length": "0",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.4(0x1800042c) NetType/4G Language/zh_CN",
        "Referer": "http://home.yngqt.org.cn/qndxx/user/guize.aspx",
        "Cookie": Cookie
    }
    try:
        r = requests.post(url, headers=headers)
        if r.ok:
            resp = r.json()
            print(resp['message'])
        else:
            print(f'发生未知错误：\n{r.text}')
    except Exception as e:
        print(e)


def main(event, context):
    with open('./config.json', 'r', encoding='utf-8') as f:
        Cookie = json.load(f)['Cookie']
    if time.localtime()[6] in [1,2,3]: # 周一、周二、周三各学习一遍
        erverWeek(Cookie)
        everyDay(Cookie)
    else:
        everyDay(Cookie)


if __name__ == '__main__':
    main("","")
