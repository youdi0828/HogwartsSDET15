#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from mitmproxy import http


def response(flow: http.HTTPFlow):
    # 加上过滤条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 把响应数据转化成python对象，保存到data中
        data = json.loads(flow.response.content)
        # 修改第一支股票的名称
        data['data']['items'][0]['quote']['name'] = "hogwarts000000001"
        data['data']['items'][1]['quote']['name'] = "hogwarts000000002"
        data['data']['items'][1]['quote']['current'] = 0.1
        # 把修改后的内容赋值给 response 原始数据格式
        flow.response.text = json.dumps(data)
