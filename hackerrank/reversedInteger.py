
def getInversedNumber(num):
	numberInBinary = bin(num)[2:]
	inverse = ''
	for i in numberInBinary:
		if i == '1':
			inverse += '0'
		else:
			inverse += '1'
	return int(inverse, 2)

def main():
	number = input()
	print getInversedNumber(number)

if __name__ == '__main__':
	main()