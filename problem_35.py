"""
https://projecteuler.net/problem=35
The answer is 55
"""
import scripts as s
def getNum(num):
	nl = list(str(num))
	l = []
	for each in nl:
		nl.insert(0, nl[-1])
		nl.pop()
		l.append(''.join(nl))
	return l

def IsCircularPrime(num):
	cir = getNum(num)
	if False in [s.IsPrime(int(x)) for x in cir]:
		return False
	else:
		return True

def main():
	num_range = s.FindPrimeInRange(1, 999999)
	cleaned_list = [ x for x in num_range if IsCircularPrime(x) ]
	print len(cleaned_list)

if __name__ == '__main__':
	main()