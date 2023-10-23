
def enroll(name, sex=6, city='BeiJing'):
	print("name:", name)
	print('sex:', sex)
	print('city:', city) 
	return None
	
enroll('caojianwei', city='shanghai')	

def calc(*number):
	sum = 0
	for n in number:
	 sum = sum + n
	return sum

sum = calc(1,2,3,4,5,6)	

print(sum)


def person(name, age, **kw):
    print(kw) 
	
	
print(person('aaa', 10))	
	