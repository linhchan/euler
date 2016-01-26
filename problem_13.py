"""
https://projecteuler.net/problem=13
The answer is 5537376230
"""
def listnum():
	file = 'number13.txt'
	f = open(file, 'r')
	sum = 0
	for each in f.readlines():
		sum += int(each.strip())
	return str(sum)[:10]

def main():
	print listnum()

if __name__ == '__main__':
	main()
