"""
http://projecteuler.net/problem=44
The answer is 5482660
"""

def getlist(n):
	lt = []
	for x in range(1,n+1):
		lt.append(x*(3*x - 1) / 2)
	return lt

def findpair():
	l = getlist(10000)
	found = False
	for x in l:
		for y in l:
			if (x+y) in l and abs(x-y) in l:
				found = True
				print x,y

	return found

def main():
	print findpair()
if __name__ == '__main__':
	main()