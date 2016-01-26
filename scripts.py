from math import sqrt as sqrt
def IsPrime(x):
    """Determine if x is prime."""
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, int(sqrt(x)) + 1):
    	if x % i == 0:
            return False
    return True

def FinePrimeInRange(a,b):
	return [x for x in range(a,b) if IsPrime(x)]

def IsPandigital(x):
	length = len(str(x))
	isP = True
	for each in str(x):
		if int(each) in range(1, length + 1):
			isP = True
		else:
			isP = False
	return isP

def FindPrimes(n):
    is_prime = list()
    limit = n
    is_prime = [False] * (limit + 1)

    for x in range(1,int(sqrt(limit))+1):
        for y in range(1,int(sqrt(limit))+1):
            n = 4*x**2 + y**2

            if n<=limit and (n%12==1 or n%12==5):
                # print "1st if"
                is_prime[n] = not is_prime[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7:
                # print "Second if"
                is_prime[n] = not is_prime[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11:
                # print "third if"
                is_prime[n] = not is_prime[n]

    for n in range(5,int(sqrt(limit))):
        if is_prime[n]:
            for k in range(n**2,limit+1,n**2):
                is_prime[k] = False
    print 2
    print 3
    for n in range(5,limit):
        if is_prime[n]: print n

def FindTriangle(n):
    lt = []
    for x in range(1,n+1):
        lt.append(x*(x + 1) / 2)
    return lt
  
def FindPentagonal(n):
    lt = []
    for x in range(1,n+1):
        lt.append(x*(3*x - 1) / 2)
    return lt

def FindHexagonal(n):
    lt = []
    for x in range(1,n+1):
        lt.append(x*(2*x - 1))n
    return lt

