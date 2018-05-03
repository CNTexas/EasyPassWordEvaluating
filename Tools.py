#!/usr/bin/env python

# encoding: utf-8

'''
@author: CNTexas
@contact: dzhx0621@gmail.com
@file: Tools.py
@time: 2018/5/3 13:52
@desc:
'''
# 保存
def saveFile(dict_name):
    #dict_name = {1: {1: 2, 3: 4}, 2: {3: 4, 4: 5}}
    f = open('temp.txt', 'w')
    f.write(str(dict_name))
    f.close()

# 读取
def readFile():
    f = open('temp.txt', 'r')
    a = f.read()
    return  eval(a)
