#!/usr/bin/env python

# encoding: utf-8

'''
@author: CNTexas
@contact: dzhx0621@gmail.com
@file: findAlphabet.py
@time: 2018/5/3 12:14
@desc:
'''
import re

def findAlphabet(line):
    mode = re.compile('[a-z]+')
    str1 = line
    #print(mode.findall(str1))
    return mode.findall(str1)