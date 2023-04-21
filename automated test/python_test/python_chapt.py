#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import base64
from PIL import Image, ImageFilter
from io import BytesIO
import ddddocr


def getCaptcha():
    url = "https://vue2.go-admin.dev/api/v1/captcha"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


def resCaptcha():
    data = getCaptcha()

    img_data = data["data"].split(",")[1]
    # 将base64编码转换为字节序列
    img_bytes = base64.b64decode(img_data)
    # 将字节序列解码为图像格式
    img = Image.open(BytesIO(img_bytes))
    ocr = ddddocr.DdddOcr()
    res = ocr.classification(img)
    return res


def resUuid():
    data = getCaptcha()

    res_uuid = data["id"]

    return res_uuid


code = resCaptcha()
uuid = resUuid()
# if __name__ == '__main__':
print("########")
print(code)
print(uuid)

'''
@version:3.8
@author:chenchen
@file:python_chapt.py
@time:2023/3/28 0:11
'''
