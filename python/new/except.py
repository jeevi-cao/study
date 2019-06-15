#!/bin/eny python 
#coding=utf-8

'''
while True:
	try:
		x = int(input('Please enter a number:'))
		break
	except ValueError:
		print("Oops! that was no valid number. Try again ")
'''

import sys

try:
	f = open('myfile.txt')
	s = f.readline()
	i = int(s.strip())
except OSError as err:
	print(type(err))
	print("OS error： {0}".format(err))
except ValueError:
	print("Cloud not convert data to an integer.")
except:
	print("UNexpected error:", sys.exc_info()[0])
	raise

