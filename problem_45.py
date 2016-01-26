"""
http://projecteuler.net/problem=45
The answer is 1533776805
"""
import scripts as s

def main():
	t = sorted(s.FindTriangle(100000))
	p = sorted(s.FindPentagonal(100000))
	h = sorted(s.FindHexagonal(100000))
	n = [x for x in t if x in p and x in h]
	print n
	
if __name__ == '__main__':
	main()

"""
Another solution using Set and took much faster

from sets import *
from time import *

def T(n):
    return (n*(n+1))/2

def P(n):
    return (n*(3*n-1))/2

def H(n):
    return n*(2*n-1)

start = clock()
Ts = Set([T(x) for x in range(286,100000)])
Ps = Set([P(x) for x in range(166,100000)])
Hs = Set([H(x) for x in range(144,100000)])

print Ts.intersection(Ps.intersection(Hs))
print "Time taken = %.2f" % (clock()-start)


Set([1533776805])
>>> print "Time taken = %.2f" % (clock()-start)
Time taken = 0.28
"""
