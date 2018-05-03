#!/usr/bin/env python

# encoding: utf-8

'''
@author: CNTexas
@contact: dzhx0621@gmail.com
@file: findSpecialWord.py
@time: 2018/5/3 12:20
@desc:
'''
import re
def findSpecial(line):
    mode = re.compile(r'\W+')
    str1 = line
    #print(mode.findall(str1))
    return mode.findall(str1)