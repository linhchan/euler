"""
https://projecteuler.net/problem=6
The answer is 25164150
"""
a = sum([i for i in range(1,101)])**2
b = sum([i**2 for i in range(1,101)])
print a-b
