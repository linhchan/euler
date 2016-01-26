import scripts as s

def FindPrime(a, b):
    """Find all primes for all x in a <= x <= b."""
    return [x for x in range(a, b + 1) if s.IsPrime(x)]

# def IsPrime(x):
#     """Determine if x is prime."""
#     if x < 2:
#         return False
#     if x == 2:
#         return True
#     for i in range(2, int(sqrt(x)) + 1):
#         if x % i == 0:
#             return False
#     return True

def FindLargestFactor(num):
    #import pdb; pdb.set_trace()
    factors = []
    prime_list = sorted(FindPrime(2,600851475143))
    for each in prime_list:
        if num % each == 0:
            #while num / each !=1:
            num = num / each
            factors.append(each)
            each = prime_list[0]
            while num == 1:
                break

    return sorted(factors)[-1]

def FindEasyLargestFactor(num):
    i = 2
    #import pdb; pdb.set_trace()
    while i**2 < num:
        while num % i ==0 :
            num = num / i
        i += 1
    return num

def main():
    #print sorted(FindPrime(2,13195))
    print FindEasyLargestFactor(600851475143)

if __name__ == '__main__':
    main()