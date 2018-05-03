#!/usr/bin/env python

# encoding: utf-8

'''
@author: CNTexas
@contact: dzhx0621@gmail.com
@file: read.py
@time: 2018/5/3 11:31
@desc:
'''
import os
from findAlphabet import *
from findNum import *
from findSpecialWord import *
from Tools import *


catelist = os.listdir("password")
#print(catelist)
maxList={1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{},9:{},10:{}}

for file_path in catelist:  # 遍历类别目录下的所有文件
    f = open("password/"+file_path)  # 返回一个文件对象
    lines = f.readlines()  # 调用文件的 readline()方法
    #print(line)
    for line in lines:
        #print(line)
        keys=findSpecial(line)
        for str in keys:
            if len(str) > 10:
                continue
            if str in maxList[len(str)].keys():
                maxList[len(str)][str]=maxList[len(str)][str]+1
            else:
                maxList[len(str)][str]= 1
        keys = findNum(line)
        for str in keys:
            if len(str) > 10:
                continue
            if str in maxList[len(str)].keys():
                maxList[len(str)][str]=maxList[len(str)][str]+1
            else:
                maxList[len(str)][str]=1
        keys = findAlphabet(line)
        for str in keys:
            if len(str)>10:
                continue
            if str in maxList[len(str)].keys():
                maxList[len(str)][str]+=1
            else:
                maxList[len(str)][str]=1
print(maxList[1].values())
print(sum(maxList[1].values()))
print(maxList[1]['q'])
print(type(maxList[1]['q']))
saveFile(maxList)
'''
words_P={}
for firstKey in maxList.keys():
    for secondKey in maxList[firstKey].keys():
        value = int(maxList[firstKey][secondKey])
        Sum=0
        for i in maxList[firstKey].values():
            Sum+=int(i)
        
        print(Sum+":::"+value)
        words_P[firstKey][secondKey]=round(value/Sum,2)
print(words_P[4]["1234"])
#print(maxList.keys())
'''