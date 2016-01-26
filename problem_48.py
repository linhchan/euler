"""
http://projecteuler.net/problem=48
The answer is 9110846700
"""

def getsum(n):
	sum = 0
	for x in range(1,n+1):
		sum = sum + x**x
	return sum

def main():
	print str(getsum(1000))[-10:]

if __name__ == '__main__':
	main()
