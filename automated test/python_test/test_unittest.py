#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
import unittest


class demo0(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownClass")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("test_case01")
        self.assertEqual(1, 1, "判断相等")

    def test_case02(self):
        print("test_case02")
        self.assertEqual(2, 2, "判断相等")

    @unittest.skipIf(1 + 1 == 2, "跳过这条用例")
    def test_case03(self):
        print("test_case03")
        self.assertEqual(3, 3, "判断相等")


class demo1(unittest.TestCase):
    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_demo1_case01(self):
        print("test_demo1_case01")

    def test_demo1_case02(self):
        print("test_demo1_case02")


class demo2(unittest.TestCase):
    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_demo2_case01(self):
        print("test_demo2_case01")

    def test_demo2_case02(self):
        print("test_demo2_case02")


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(demo0('test_case01'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    suite01 = unittest.TestLoader().loadTestsFromTestCase(demo0)
    suite02 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    suite_all = unittest.TestSuite([suite01, suite02])
    runner = unittest.TextTestRunner()
    runner.run(suite_all)

'''
@version:3.8
@author:chenchen
@file:test_unittest.py
@time:2023/3/24 16:36
'''
