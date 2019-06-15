#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student(object):
     __slots__ = ('name', 'age')
	 
	 
s = Student()
s.name = 'cjw'
s.age = 10

#s.score = 20

print(s);