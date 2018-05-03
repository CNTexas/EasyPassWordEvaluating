#!/usr/bin/env python

# encoding: utf-8

'''
@author: CNTexas
@contact: dzhx0621@gmail.com
@file: Main.py
@time: 2018/5/3 13:55
@desc:
'''
from Tools import *
from findAlphabet import *
from findNum import *
from findSpecialWord import *
import math

maxList= readFile()
print(maxList[1]['q']/sum(maxList[1].values()))
TestPassword=input("输入一个字符串：")
words={}
for str in findAlphabet(TestPassword):
    if str in maxList[len(str)].keys():
        words[str]=maxList[len(str)][str]/sum(maxList[len(str)].values())
    else:
        words[str]=1
for str in findNum(TestPassword):
    if str in maxList[len(str)].keys():
        words[str]=maxList[len(str)][str]/sum(maxList[len(str)].values())
    else:
        words[str]=1
for str in findSpecial(TestPassword):
    if str in maxList[len(str)].keys():
        words[str]=maxList[len(str)][str]/sum(maxList[len(str)].values())
    else:
        words[str]=1
print(words)
P=1
for i in words.values():
    P*=i
P=-math.log(P)
print(P)
