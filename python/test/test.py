 

'''
for i in range(1, 10):
	print('\n')
	for j in range(1, i+1):
		print("%d*%d=%d " % (i, j, i * j),  end=' ')

'''

n = int(input('n = '))
a = int(input('a = '))
sum = 0
total = 0
for i in range(n):
    sum += (10 ** i)
    print(sum)
    total += sum * a
print(total)