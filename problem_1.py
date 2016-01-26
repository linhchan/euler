"""
https://projecteuler.net/problem=1
The answer is 233168
"""
def summe(num):
    sum = 0
    for x in range(0,num):
        if x %3 ==0 or x %5 ==0:
            sum = sum + x
    return sum

def main():
    print summe(1000)

if __name__ == '__main__':
	main()
