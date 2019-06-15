#!/bin/env python 
#coding=utf-8

'''
class Myclass:
	i = 123456
	def f(self):
		return 'hello world!'



x = Myclass()
print('Myclass 类的属性 I 为', x.i)
print('Myclass 类的方法 I 为', x.f())
'''

'''
class people:
	name = ''
	age = 0
	__weight = 0

	def __init__(self, n, a, w):
		self.name = n
		self.age = a 
		self.__weight = w

	def speak():
		print("%s 说: 我 %d 岁。" %  (self.name, self.age))


p = people('曹建伟', 10, 100)

print(p.name)
'''
class Vector:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __str__(self):
		return 'Vector (%d, %d) is ' % (self.a , self.b)

	def __add__(self, other):
		return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)

print(v1)
print(v1 + v2)