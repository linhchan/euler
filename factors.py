from math import sqrt as sqrt
def FactorSize(n):
	lt = []
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			lt.append(i)
			lt.append(n/i)
	return len(sorted(list(set(lt))))
