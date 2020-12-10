#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from mitmproxy import http


def response(flow: http.HTTPFlow):
    # 加上过滤条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 把响应数据转化成python对象，保存到data中
        data = json.loads(flow.response.content)
        # 对第一个股票保持原样
        # 对第二个股票名字加长一倍
        # 对第三个股票名字变成空
        name2 = data['data']['items'][1]['quote']['name']
        data['data']['items'][1]['quote']['name'] = name2 * 2
        data['data']['items'][2]['quote']['name'] = ""
        # 把修改后的内容赋值给 response 原始数据格式
        flow.response.text = json.dumps(data)
