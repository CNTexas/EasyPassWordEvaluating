#!/usr/bin/env python

# encoding: utf-8

'''
@author: CNTexas
@contact: dzhx0621@gmail.com
@file: findNum.py
@time: 2018/5/3 12:10
@desc:
'''
import re
def findNum(line):
    mode = re.compile(r'\d+')
    str1 = line
    #print(mode.findall(str1))
    return mode.findall(str1)