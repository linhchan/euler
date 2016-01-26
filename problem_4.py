"""
https://projecteuler.net/problem=4
The answer is 906609
"""
def isPalindrome(num):
	org_num = num
	r_num = 0
	while num != 0:
		last_digit = num % 10
		r_num = (r_num *10) + last_digit
		num = num / 10
	return True if r_num == org_num else False

def Product(a,b):
    pl = []
    for x in range(a,b):
        for y in range(a,b):
            if isPalindrome(x*y) :
            	pl.append(x*y)
    return pl

def main():
	print sorted(Product(100,1000))[-1]

if __name__ == '__main__':
	main()