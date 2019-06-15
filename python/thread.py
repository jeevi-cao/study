#!/bin/env python 
#coding=utf-8
'''
import threading
import time
'''
'''
def print_time(threadName, delay):
	count = 0
	print(threadName)
	while count < 5:
		time.sleep(delay)
		count += 1
		print("%s %s" % (threadName, time.ctime(time.time())))


try:
	_thread.start_new_thread( print_time, ("thread-1", 2))
	_thread.start_new_thread( print_time, ("thread-2", 4))
	_thread.start_new_thread( print_time, ("thread-3", 6))
except:
	pirnt("Error:　无法启动线程")
'''
'''
exitFlag = 0

class MyThread (threading.Thread): 


	def __init__(self, threadId, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadId
		self.name = name
		self.counter = counter

	def run(self):
		print("开始线程" + self.name)
		print_time(self.name, self.counter, 5)
		print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
	while counter:
		if exitFlag:
			threadName.exit()
		time.sleep(delay)
		print ("%s: %s" % (threadName, time.ctime(time.time())))
		counter -= 1



thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(1, "Thread-2", 2)

thread1.start();
thread2.start()
thread1.join()
thread2.join()
print ("退出主线程")
'''
'''
import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
'''

import threading
from time import sleep, ctime

def loop():
	pass

print(dir(loop))
