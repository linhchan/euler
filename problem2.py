def fib(n):
	a,b = 1,1
	l = []
	for i in range(n):
		a,b = b,a+b
		l.append(a)
	return a,l

def main():
	fib_num, l_f = fib(4000000)
	
	print fib_num, l_f[4000000]

if __name__ == '__main__':
	main()