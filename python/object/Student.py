#!/usr/bin/env python 
# -*- coding: utf-8 -*-

class Student(object):

	@property
    def birth(self):
        return self._birth 
	@property.setter
	def birth(self, value):
        self._birth = value
	   
	@property
	def age(self):
        return self._age;
	   
	   
s = Student();

s.birth = 20
print(s.birth)
s.age = 30
print(s.age)