#!/bin/env python 
#--**-- coding:utf-8 --*--

import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'(a.*) are (.*?) .*', line, re.M|
	re.I)

if matchObj:
	print("matchObj.group() : ", matchObj.group())
	print("matchObj.group() : ", matchObj.group(1))
	print("matchObj.group() : ", matchObj.group(2))
	print("matchObj.group() : ", matchObj.groups())
else: 
    print("No match!!")