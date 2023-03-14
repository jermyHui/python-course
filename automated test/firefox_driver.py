#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
import time

import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.common.by import By
# def test_selenium():
# s = Service("D:\software\foxdriver\geckodriver.exe")
driver = webdriver.Firefox()
driver.get('https://www.baidu.com/')
time.sleep(8)
'''
@version:3.8
@author:chenchen
@file:firefox_driver.py
@time:2023/3/13 14:57
'''
