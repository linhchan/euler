"""
https://projecteuler.net/problem=7
Not my solution. The answer is 104743
"""

import time, math
s = time.time()
def IsPrime( n ):
    if n == 2:
        return 1
    elif n % 2 == 0:
        return 0
    
    i = 3
    range = int( math.sqrt(n) ) + 1
    while( i < range ):
        if( n % i == 0):
            return 0
        i += 1
    return 1
N,T = 1,3
while N < 10001:
    if IsPrime(T):
        N+=1
    T+=2
print T-2
print time.time() - s


# def Prime():
#     number = 1
#     prime = 1
#     divide = None
#     while number < 10001:
#         prime = prime+2
#         divide=1
#         while True:
#             divide=divide + 2
#             if prime == divide:
#                 number += number
#                 break
#             elif prime%divide == 0 and prime != divide:
#                 break
#     return (number, prime)

# def FindPrime(a, b):
#   """Find all primes for all x in a <= x <= b."""

#   return [x for x in range(a, b + 1) if IsPrime(x)]

# def IsPrime(x):
#   """Determine if x is prime."""

#   if x < 2:
#     return False

#   if x == 2:
#     return True

#   for i in range(2, int(sqrt(x)) + 1):
#     if x % i == 0:
#       return False

#   return True

#def main():
#    n,p = Prime()
#    print "The %d prime is: %d" %(n,p)
 
  #lt = FindPrime(2, 104810)
  #print lt.index(104743)
  #print lt[-1::-1]

#if __name__ == '__main__':
#  main()