#!/bin/env python3
#coding=utf-8
'''
from multiprocessing import Process
import os, time
'''
'''
print("Run task %s  ..." % (os.getpid()))

pid = os.fork()

if pid == 0:
	print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
	print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''
'''
def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))
	time.sleep(2)
	print("Child process end.")


if __name__=='__main__':
	print('Parent process %s.' % os.getpid());
	p = Process(target=run_proc, args=('test',)) 
	p.start()
	p.join()
	print("end  parent process end.")
'''
 
from multiprocessing import Pool
import os, time, random

age = 10;

def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    #age = time.time()
    kk = age;
    kk += 1;
    end = time.time()
    print('Task %s runs %0.2f seconds. age = %s' % (name, (end - start), kk))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(5)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done. age=%s' % age)
 
 