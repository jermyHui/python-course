#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
import json

import requests
import python_chapt

url = 'https://vue2.go-admin.dev/api/v1/login'
payload = json.dumps({
    "username": "admin",
    "password": "123456",
    "rememberMe": "false",
    "code": python_chapt.code,
    "uuid": python_chapt.uuid
})
headers = {
    'Content-Type': 'application/json'
}
response = requests.request("POST", url, data=payload, headers=headers)

if __name__ == '__main__':
    print(type(python_chapt.code))
    print(type(python_chapt.uuid))
    print(response.text)

'''
@version:3.8
@author:chenchen
@file:loginurl_test.py
@time:2023/3/27 23:15
'''
