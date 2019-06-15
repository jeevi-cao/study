#!/bin/env python
# --*-- coding:utf-8 --*--

Money = 100

def AddMondy():
	global Money
	Money = Money + 1

print(Money)
AddMondy()
print(Money)