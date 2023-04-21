#!/usr/bin/env python3.8
# -*- coding: UTF-8 -*-
import _thread
import logging
import threading
from time import ctime, sleep

logging.basicConfig(level=logging.INFO)

loops = [2, 4]


def loop(nloop, nsce):
    logging.info("loop" + str(nloop) + " start at " + ctime())
    sleep(nsce)
    logging.info("loop" + str(nloop) + " end at " + ctime())

def main():
    logging.info("loop all start at " + ctime())
    nloops = range(len(loops))
    threads = []
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("loop all end at " + ctime())

if __name__ == '__main__':
    main()


'''
@version:3.8
@author:chenchen
@file:main.py
@time:2023/3/16 22:51
'''
