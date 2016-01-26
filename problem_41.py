"""
NOT FINISHED
"""
import scripts as s
def test():
	prime_range = s.FinePrimeInRange(1,999999)
	pprime = [x for x in prime_range if s.IsPandigital(x)]
	return sorted(pprime)[-1]


def main():
	print s.FindPrimes(1000000000)
if __name__ == '__main__':
	main()