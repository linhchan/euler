"""
 https://projecteuler.net/problem=20
 The answer is 648
"""
from math import factorial as f
print sum([int(x) for x in str(f(100))])