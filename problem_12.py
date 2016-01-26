import factors as f
def FindTriangleNumbers(n): #1, 3, 6, 10, 15, 21, 28, 36, 45, 55
	lt = range(n)
	new = [0]
	#import pdb; pdb.set_trace()
	for x in lt: #[0,1,2,3,4,5,6,7,8,9]
		x_index = lt.index(x) + 1
		new.append(new[-1] + x_index)
	return new

def main():
	for x in FindTriangleNumbers(15000):
		if f.FactorSize(x) > 500:
			print x, f.FactorSize(x)
	

if __name__ == '__main__':
	main()