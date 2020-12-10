#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    # 修改判断条件
    if "quote.json" in flow.request.pretty_url:
        # 打开保存在本地的数据文件
        with open("/Users/youdi/PycharmProjects/HogwartsSDET15/mitmproxy/respones.json") as f:
            # 创造一个 response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # 读取文件中的数据作为返回内容
                {"Content-Type": "application/json"}  # (optional) headers
            )
