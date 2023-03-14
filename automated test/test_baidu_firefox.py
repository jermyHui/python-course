#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
import time

import selenium
from selenium import webdriver

# from selenium.webdriver.common.by import By
# def test_selenium():
from selenium.webdriver.common.by import By


class AutomatedTest:
    def setup(self):
        # s = Service("D:\software\foxdriver\geckodriver.exe")
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_case(self, forumList=None):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.LINK_TEXT, '贴吧').click()
        self.driver.find_element(By.LINK_TEXT, '高校精选专题').click()
        self.driver.find_element(By.LINK_TEXT, '清华大学').click()

at = AutomatedTest()
at.setup()
at.test_case()
at.teardown()

'''
@version:3.8
@author:chenchen
@file:test_baidu_firefox.py
@time:2023/3/13 15:22
'''
