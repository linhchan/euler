"""
 https://projecteuler.net/problem=29
 The answer is 9183
"""

def Dis():
	a,b = 2, 101
	list_num = []
	for x in range(a,b):
		for y in range(a,b):
			list_num.append(x**y)

	return list(set(list_num))

def main():
	print len(Dis())

if __name__ == '__main__':
	main()