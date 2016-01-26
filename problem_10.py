"""
https://projecteuler.net/problem=10
The answer is 142913828922
"""
import scripts as s

def FindSumPrime(a, b):
    primelist = [x for x in range(a, b + 1) if s.IsPrime(x)]
    return sum(primelist)

def main():
    print FindSumPrime(0, 2000000)
if __name__ == '__main__':
    main()
