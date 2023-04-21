#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
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

def getLoginData():
    data = getCaptcha()

    uuid = data["id"]

    img_data = data["data"].split(",")[1]
    # 将base64编码转换为字节序列
    img_bytes = base64.b64decode(img_data)
    # 将字节序列解码为图像格式
    img = Image.open(BytesIO(img_bytes))

    ocr = ddddocr.DdddOcr()
    res = ocr.classification(img)
    print("########")

    return uuid, res


def main():
    url = "https://vue2.go-admin.dev/api/v1/login"
    uuid, code = getLoginData()
    payload = json.dumps({
        "username": "admin",
        "password": "123456",
        "rememberMe": False,
        "code": code,
        "uuid": uuid
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    print(type(code))
    print(type(uuid))

    print(response.text)


if __name__ == '__main__':
    print("222222222222222222")
    main()
'''
@version:3.8
@author:chenchen
@file:url_test.py
@time:2023/3/30 16:23
'''
