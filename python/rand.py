# -*- coding: utf-8 -*-
import random

# 带权重的随机
def __in_which_part(n, w):
	print 'n:', n
	for i, v in enumerate(w):
		if n < v:
			return i
	return len(w) - 1
 
def weighting_choice(data, weightings):
	s = sum(weightings)
	w = [float(x)/s for x in weightings]
 
	t = 0
	for i, v in enumerate(w):
		t += v
		w[i] = t
        print 'w:', w
	c = __in_which_part(random.random( ), w)
	try:
		return data[c]
	except IndexError:
		return data[-1]
		


print 'weighting_choice', weighting_choice(['a', 'b', 'c', 'e','d'], [10, 10, 20, 30 , 60, 70])
