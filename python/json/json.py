#!/bin/env python 
#coding=utf-8
import json

data = {
	'no' : 1,
	'name': 'Runoob',
	'url' : ''
}

json_str = json.dumps(data) 
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)
