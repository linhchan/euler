"""
http://projecteuler.net/problem=14
The answer is 837799

linhchan@Linhs-MacBook-Pro:~/Euler$ time python problem_14.py 
Number 525 produces longest chains of 837799

real	1m9.522s
user	1m9.088s
sys	0m0.262s

"""

def Even(num):
	return num /2

def Odd(num):
	return 3*num + 1

def Sequence(n):
	lt = [n]
	while n !=1:
		if n % 2 == 0:
			n = Even(n)
		else:
			n = Odd(n)
		lt.append(n)
	return lt

def main():
	dict1 = {}
	for i in range(1,1000000):
		dict1[i] = len(Sequence(i))
	startnum, chain = sorted([(value,key) for (key,value) in dict1.items()])[-1]
	print 'Number %d produces longest chains of %d' %(startnum,chain)

if __name__ == '__main__':
	main()
