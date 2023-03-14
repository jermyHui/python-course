#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# def test_selenium():
s = Service("D:\software\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://www.baidu.com/')
time.sleep(8)
'''
@version:3.8
@author:chenchen
@file:selenium_import.py
@time:2023/3/12 23:55
'''
